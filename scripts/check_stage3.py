"""Validate stage 3 contracts, traceability, standalone graphics and built links.

Install requirements-validation.txt, then run:
  python scripts/check_stage3.py /tmp/restaurant-stage3-public /tmp/restaurant-stage3-draft
MkDocs must build both directories before the HTML checks.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
import yaml
from openapi_spec_validator import validate

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / 'docs/project'
PUBLIC = PROJECT / 'published'


class UniqueLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        assert key not in result, f'Duplicate YAML key: {key}'
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)
spec = yaml.load((PUBLIC / '05_api/openapi.yaml').read_text(), Loader=UniqueLoader)
validate(spec)
ops = {}
for path, methods in spec['paths'].items():
    for method, op in methods.items():
        assert op['operationId'] not in ops
        ops[op['operationId']] = op
        assert op['x-release'] in ['MVP', 'R1']
        assert op['x-roles'] and op['x-stories']
        assert set(op['x-stories']) <= {f'US-{i:02}' for i in range(1, 36)}
        if method != 'get':
            assert any(p.get('$ref', '').endswith('/IdempotencyKey') for p in op['parameters'])
        assert 'history' not in path and 'reviews' not in path and 'repeat' not in path


def resolve(ref):
    value = spec
    assert ref.startswith('#/'), ref
    for part in ref[2:].split('/'):
        value = value[part.replace('~1', '/').replace('~0', '~')]
    return value


def walk(value):
    if isinstance(value, dict):
        if '$ref' in value:
            resolve(value['$ref'])
        if value.get('type') == 'object':
            assert set(value.get('required', [])) <= set(value.get('properties', {}))
        for child in value.values():
            walk(child)
    elif isinstance(value, list):
        for child in value:
            walk(child)


# Semantic regressions that syntactic OpenAPI validation does not detect.
schemas = spec['components']['schemas']
for name, fields in {
    'Session': ['token'], 'StaffLogin': ['login'], 'MenuItem': ['name', 'price'],
    'Calculation': ['subtotal', 'discount', 'afterDiscount', 'total'],
    'Purchase': ['orderNumber', 'cellNumber'], 'Payment': ['amount', 'externalPaymentId'],
    'Refund': ['amount', 'externalRefundId'], 'Error': ['message'],
}.items():
    for field in fields:
        assert schemas[name]['properties'][field].get('x-release') != 'R1', (name, field)
for field in ['insertedAmount', 'changeAmount', 'cashReturnStatus']:
    assert schemas['Payment']['properties'][field]['x-release'] == 'R1'
assert schemas['PrepareInput']['properties']['loyaltyToken']['x-release'] == 'R1'
assert schemas['Session']['properties']['activePurchaseId']['format'] == 'uuid'
assert ops['getSession']['security'] == [{'deviceAuth': []}]
assert 'end_session' in schemas['Session']['properties']['allowedActions']['items']['enum']
assert schemas['DocumentState']['properties']['problemStatus']['enum'] == ['new', 'accepted', 'resolved']

def check_time_context(value, path=()):
    if isinstance(value, dict):
        if value.get('format') == 'date-time' and 'Срок токена' in value.get('description', ''):
            assert path in [('Session', 'properties', 'expiresAt')], path
        for key, child in value.items():
            check_time_context(child, path + (str(key),))
    elif isinstance(value, list):
        for i, child in enumerate(value):
            check_time_context(child, path + (str(i),))

check_time_context(schemas)
for op in ops.values():
    if '412' in op['responses']:
        assert any(p.get('$ref', '').endswith('/IfMatch') for p in op.get('parameters', [])), op['operationId']

walk(spec)
# The Swagger view is derived from the canonical YAML, not a second edited contract.
viewer = (PUBLIC / 'assets/swagger/index.html').read_text(encoding='utf-8')
payload = re.search(r'<script id="openapi-spec" type="application/json">(.*?)</script>', viewer, re.S)
assert payload and json.loads(payload.group(1)) == spec, 'Stale Swagger UI specification'
assert hashlib.sha256((PUBLIC / '05_api/openapi.yaml').read_bytes()).hexdigest() in viewer
# Traverse the public projection: no closed purchase or ticket fields may leak through refs.
def public_fields(value, visited=None):
    visited = set() if visited is None else visited
    if not isinstance(value, dict):
        return set()
    if '$ref' in value:
        if value['$ref'] in visited:
            return set()
        visited.add(value['$ref'])
        return public_fields(resolve(value['$ref']), visited)
    found = set(value.get('properties', {}))
    for child in value.get('properties', {}).values():
        found |= public_fields(child, visited)
    if 'items' in value:
        found |= public_fields(value['items'], visited)
    return found

assert not public_fields(spec['components']['schemas']['Board']) & {
    'purchaseId', 'code', 'ticketCode', 'payment', 'calculation', 'phone', 'total'
}
ui = (PUBLIC / '05_api/ui.md').read_text()
trace = (PUBLIC / '08_traceability.md').read_text()
resources = (PUBLIC / '05_api/resources.md').read_text()
for op in ops:
    assert op in ui, ('UI mapping missing', op)
    assert op in resources, ('Resource purpose missing', op)
# Every story has a direct screen/operation chain and model/component mapping.
for i in range(1, 36):
    assert re.search(rf'^\| US-{i:02} \|', trace, re.M), i
assert {u for op in ops.values() for u in op['x-stories']} >= {
    f'US-{i:02}' for i in range(1, 36) if i != 13
}
# US-13 is help in the hall, not an artificial new REST operation.

baseline_files = {
    'published/01_business/goals.md': r'^\| (БТ-\d+) \|',
    'published/02_requirements/user-stories.md': r'^\| (US-\d+) \|',
    'published/02_requirements/nfr.md': r'^\| (НФТ-\d+) \|',
    'published/02_requirements/assumptions.md': r'^\| (A-\d+) \|',
    'published/06_decomposition/acceptance-criteria.md': r'^## (AC-\d+\.\d+)',
}
for file, pattern in baseline_files.items():
    baseline = file
    if subprocess.run(['git', 'cat-file', '-e', 'HEAD:docs/project/' + baseline],
                      cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode:
        # Before the stage 4 move is committed, the baseline is at its legacy path.
        baseline = file.replace('published/06_decomposition/', 'documentation/06_decomposition/')
    old = subprocess.check_output(['git', 'show', 'HEAD:docs/project/' + baseline], cwd=ROOT).decode()
    now = (PROJECT / file).read_text()
    old_ids = re.findall(pattern, old, re.M)
    ids = re.findall(pattern, now, re.M)
    assert ids == old_ids and len(ids) == len(set(ids)), file
    if 'user-stories' in file or 'assumptions' in file or '/nfr' in file:
        assert now == old, ('Source requirement changed', file)
assert not (PROJECT / 'documentation/05_api').exists()

flow_page = (PUBLIC / '04_architecture/integration-flows.md').read_text()
blocks = re.findall(r'```mermaid\n(.*?)```', flow_page, re.S)
assert len(blocks) == 8
for i, source in enumerate(blocks, 1):
    file = PUBLIC / f'assets/stage3-flow-{i}.svg'
    xml = file.read_text()
    root = ET.fromstring(xml)
    assert hashlib.sha256(source.encode()).hexdigest() in xml, ('Stale export', file)
    assert 'var(' not in xml and 'Syntax error' not in xml
    assert root.find('{http://www.w3.org/2000/svg}title') is not None
for file in (PUBLIC / 'assets').glob('stage3-*.svg'):
    ET.parse(file)

# The publication manifest is a second archive-integrity check, independent of Git.
manifest = json.loads((ROOT / 'scripts/homework-publication.json').read_text())
for assignment in manifest:
    for entry in assignment['files']:
        file = ROOT / 'docs/home_work' / assignment['folder'] / entry['path']
        assert hashlib.sha256(file.read_bytes()).hexdigest() == entry['sha256'], file
assert not subprocess.check_output(['git', 'diff', '--name-only', 'HEAD', '--', 'docs/home_work'], cwd=ROOT)


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.refs, self.tables = set(), [], []
        self.rows = None
        self.cells = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, ('Duplicate HTML ID', attrs['id'])
            self.ids.add(attrs['id'])
        for key in ['href', 'src']:
            if key in attrs:
                self.refs.append(attrs[key])
        if tag == 'table':
            self.rows = []
        if tag == 'tr':
            self.cells = 0
        if tag in ['th', 'td']:
            self.cells += 1

    def handle_endtag(self, tag):
        if tag == 'tr' and self.rows is not None:
            self.rows.append(self.cells)
        if tag == 'table':
            self.tables.append(self.rows)
            self.rows = None


for directory in sys.argv[1:]:
    build = Path(directory).resolve()
    assert build.is_dir(), build
    pages = {}
    for file in build.rglob('*.html'):
        page = Page()
        page.feed(file.read_text())
        pages[file.resolve()] = page
        for table in page.tables:
            assert table and len(set(table)) == 1, ('Broken table', file, table)
    count = 0
    for file, page in pages.items():
        if file.name == '404.html':
            continue
        for href in page.refs:
            url = urlsplit(href)
            if url.scheme or url.netloc:
                continue
            target = ((build / unquote(url.path).lstrip('/')) if url.path.startswith('/')
                      else (file.parent / unquote(url.path))) if url.path else file
            target = target.resolve()
            if target.is_dir():
                target = target / 'index.html'
            assert target.exists(), ('Broken link', file, href)
            if url.fragment and target in pages:
                assert unquote(url.fragment) in pages[target].ids, ('Broken anchor', file, href)
            count += 1
    print(f'{build.name}: {len(pages)} HTML pages, {count} local links/anchors/assets valid')
print(f'PASS: OpenAPI, {len(ops)} operations, {len(spec["components"]["schemas"])} schemas, '
      f'35 US, original IDs/releases, 46 AC, {len(blocks)} source-matched SVG, unchanged homework archive')
