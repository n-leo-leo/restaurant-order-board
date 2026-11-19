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

# Keep the manager lookup, reprint and display acknowledgement usable by their screens.
search = {param['name']: param for param in ops['findPurchases']['parameters'] if 'name' in param}
assert search['localDate']['schema']['format'] == 'date'
assert search['orderNumber']['schema']['type'] == 'string'
staff_detail = ops['getStaffPurchase']['responses']['200']['content']['application/json']['schema']
assert staff_detail['$ref'] == '#/components/schemas/StaffPurchase'
assert {'purchase', 'kioskId', 'kioskLabel'} <= set(resolve(staff_detail['$ref'])['required'])
assert schemas['Reprint']['required'] == ['verificationId']
ack = ops['confirmProblemDisplay']
assert ack['security'] == [{'staffAuth': []}] and ack['x-roles'] == ['manager']
assert ack['x-release'] == 'MVP'
ack_input = ack['requestBody']['content']['application/json']['schema']
assert 'displayedAt' in ack_input['required'] and ack_input['properties']['displayedAt']['format'] == 'date-time'
assert {'created', 'not_started', 'processing', 'unknown'} <= set(schemas['Payment']['properties']['status']['enum'])
assert {'held', 'expired'} <= set(schemas['Reservation']['properties']['status']['enum'])

# The manager can recover the actual destination of a reprint and the result of a conditional stop.
reprint_result = ops['reprintTicket']['responses']['202']['content']['application/json']['schema']
assert reprint_result == schemas['StaffPurchase']['properties']['lastTicketReprint']
assert {'operationId', 'printerDeviceId', 'printerKioskLabel'} <= set(resolve(reprint_result['$ref'])['required'])
visibility = ops['recordBoardVisibility']
assert visibility['security'] == [{'deviceAuth': []}] and visibility['x-roles'] == ['board']
interval = resolve(visibility['requestBody']['content']['application/json']['schema']['$ref'])
assert set(interval['required']) == {'assignmentId', 'projectionVersion', 'visibleFrom', 'visibleUntil', 'clockErrorMs'}
assert interval['properties']['clockErrorMs']['minimum'] == 0
assert 'ticketHandedAt' in schemas['Resolution']['properties']
assert 'lastTicketReprint' not in schemas['Purchase']['properties']
cancel_input = ops['cancelOrder']['requestBody']['content']['application/json']['schema']
assert 'basis' in resolve(cancel_input['$ref'])['required']
check = schemas['Purchase']['properties']['cancellationCheck']
assert check['x-release'] == 'R1' and set(check['enum']) == {'pending', 'already_started', 'stopped_before_start'}
assert {'200', '202', '204'} <= ops['createExport']['responses'].keys()
assert schemas['Export']['properties']['operationIds']['uniqueItems']
assert 'created' in ops['endSession']['description']

# Screen contracts used before starting payment and exporting the selected trading day.
assert 'availablePaymentMethods' in schemas['Session']['required']
assert schemas['Session']['properties']['availablePaymentMethods']['items']['enum'] == ['card', 'cash']
assert 'tradingDays' in schemas['Report']['required']
days = schemas['Report']['properties']['tradingDays']['items']
assert set(days['required']) == {'tradingDayId', 'localDate', 'closed', 'unbatchedOperationCount'}
assert days['properties']['unbatchedOperationCount']['minimum'] == 0
assert days['properties']['latestExportId']['format'] == 'uuid'
assert days['properties']['tradingDayId'] == schemas['ExportInput']['properties']['tradingDayId']
supply = schemas['Production']['properties']['robots']['items']['properties']['supplies']['items']
percent = supply['properties']['remainingPercent']
assert (percent['type'], percent['multipleOf'], percent['minimum'], percent['maximum']) == ('number', 0.01, 0, 100)

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
# The last reviewed four-stage revision is independent of the current checkout.
baseline_revision = '7d0003643b1822388d31b7ecb0bf8bdb56639d4b'


def requirement_rows(source, pattern):
    return {line.split('|')[1].strip(): [cell.strip() for cell in line.split('|')[1:-1]]
            for line in source.splitlines() if re.match(pattern, line)}


for file, pattern in baseline_files.items():
    old = subprocess.check_output(['git', 'show', f'{baseline_revision}:docs/project/{file}'], cwd=ROOT).decode()
    now = (PROJECT / file).read_text()
    old_ids = re.findall(pattern, old, re.M)
    ids = re.findall(pattern, now, re.M)
    assert ids == old_ids and len(ids) == len(set(ids)), file
    if 'user-stories' in file or '/nfr' in file:
        original = requirement_rows(old, pattern)
        current = requirement_rows(now, pattern)
        for identifier, cells in current.items():
            # Source citations can be edited. Story text, release, business requirements,
            # NFR category and measurable conditions retain their reviewed values.
            if identifier == 'НФТ-20':
                expected = original[identifier].copy()
                expected[2] = expected[2].replace('После удаления из ячейки заказа, который гость не забрал, ячейка может освободиться, но заказ остается завершенным по неявке.', 'После удаления еды и контроля ячейку можно освободить. Исход заказа определяется по событиям выдачи и условиям AC-16.1.')
                assert cells[:-1] == expected[:-1], identifier
            elif identifier == 'НФТ-11':
                assert cells[:2] == original[identifier][:2]
                assert cells[2] == (
                    'Не менее половины участников завершают заказ за 3 мин или быстрее. Время считается от начала '
                    'сессии до успешной оплаты. Для предварительной проверки 10 представителей целевой аудитории '
                    'проходят одинаковый сценарий без помощи. Критерий — не менее 5 из всех 10 участников. '
                    'Незавершенный заказ остается в знаменателе. Причины незавершения и банковские сбои '
                    'фиксируются отдельно.'
                ), identifier
            else:
                assert cells[:-1] == original[identifier][:-1], identifier
            if '/nfr' in file:
                # The basis column also contains acceptance conditions and assumption status.
                basis = original[identifier][-1].replace('ДЗ 13', 'Прогноз нагрузки сети')
                basis = basis.replace('ДЗ 05', 'Кейс ресторана').replace('ДЗ 07, US 20', 'Требования к мониторингу производства')
                assert cells[-1] == basis, identifier
            else:
                # Keep cross-references to project assumptions when editing course citations.
                assert re.findall(r'A-\d+', cells[-1]) == re.findall(r'A-\d+', original[identifier][-1]), identifier
    if 'assumptions' in file:
        approved = old.replace('Не менее половины заказов оформляются за 3 минуты или быстрее.',
                               'В проверке с 10 участниками не менее 5 завершают заказ за 3 минуты или быстрее. '
                               'В знаменателе остаются все 10, в том числе участники с банковским сбоем или незавершенным заказом.')
        # Only the reviewed hold, pickup and printer rules may differ from the baseline.
        for previous, revised in [
            ('Еда доступна 10 минут после первого появления номера в «Готов».', 'Срок хранения истекает через 10 минут после первого показа номера в «Готов».'),
            ('До запуска его и условия хранения проверяет технолог.', 'До запуска технолог проверяет срок и условия хранения. Допуск проверяют на оборудовании и согласуют с рестораном.'),
            ('Срок 10 минут принят как допущение.', 'Срок 10 минут и допуск 1 с на первичное включение доступа приняты как допущения.'),
            (
                'Заказ завершается по неявке. Автоматический возврат и повторное приготовление не выполняются.',
                'Неявка без автоматического возврата и повторного приготовления допустима при подтвержденных условиях AC-16.1. Талон выдан к первому показу, номер виден до конца срока, исправный доступ включен не позднее чем через 1 с и сохраняется до конца срока. Полной выдачи не было. При нарушении окна и подтвержденном неполучении применяется A-12.',
            ),
            (
                'Резерв до запуска платежа действует 5 мин.',
                'До удержания резерв действует 5 мин. До вызова банка склад подтверждает удержание за исходной попыткой оплаты. Если ответ потерян, приложение сверяет ту же операцию.',
            ),
            (
                'Менеджер повторно печатает талон через исправный принтер киоска.',
                'Менеджер запрашивает повторную печать. Сервер выбирает исправный принтер киоска того же ресторана и сохраняет его идентификатор и обозначение киоска в задаче печати. На S-02 менеджер видит место печати и фиксирует вручение копии гостю.',
            ),
        ]:
            assert approved.count(previous) == 1
            approved = approved.replace(previous, revised)
        assert now == approved, ('Source assumption changed', file)
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
