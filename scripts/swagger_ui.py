"""Build a local Swagger UI from the single canonical OpenAPI YAML.

CLI: python scripts/swagger_ui.py [--check]
MkDocs hook: refreshes the built viewer after either documentation build.
The generated source viewer also opens directly as a local HTML file.
"""
from pathlib import Path
import argparse
import hashlib
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / 'docs/project/published'
SPEC = PUBLIC / '05_api/openapi.yaml'
VIEWER = PUBLIC / 'assets/swagger/index.html'


def render(spec_path):
    source = Path(spec_path).read_text(encoding='utf-8')
    spec = yaml.safe_load(source)
    payload = json.dumps(spec, ensure_ascii=False, separators=(',', ':')).replace('<', r'\u003c')
    digest = hashlib.sha256(source.encode('utf-8')).hexdigest()
    return '''<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Swagger UI — Робот и точка</title>
<meta name="description" content="Клиентский API: операции, запросы, ответы и схемы MVP и первого релиза.">
<link rel="stylesheet" href="vendor/swagger-ui.css">
<style>
body { margin:0; background:#fafafa; }
.viewer-header { border-bottom:1px solid #d6dee5; background:#fff; padding:18px 30px;
 font:15px/1.5 Arial,sans-serif; display:flex; align-items:center; gap:24px; flex-wrap:wrap; }
.viewer-header strong { color:#243746; font-size:19px; margin-right:auto; }
.viewer-header a { color:#245b8c; }
.viewer-header span { color:#5e6b76; font-size:13px; }
.swagger-ui .info { margin:30px 0; }
.swagger-ui .topbar { display:none; }
</style>
</head>
<body>
<header class="viewer-header">
<strong>Робот и точка · Swagger UI</strong>
<span>Просмотр проектируемого контракта</span>
<a id="docs-link" href="../../05_api/openapi/">К документации API</a>
<a id="yaml-link" href="../../05_api/openapi.yaml" download="openapi.yaml">Скачать YAML</a>
</header>
<main id="swagger-ui"></main>
<noscript>Для просмотра Swagger UI включите JavaScript. Исходная спецификация доступна по ссылке «Скачать YAML».</noscript>
<!-- OpenAPI SHA256: ''' + digest + ''' -->
<script id="openapi-spec" type="application/json">''' + payload + '''</script>
<script src="vendor/swagger-ui-bundle.js" charset="utf-8"></script>
<script>
if (location.protocol === 'file:') {
 document.getElementById('docs-link').href = '../../05_api/openapi.md';
}
window.ui = SwaggerUIBundle({
 spec: JSON.parse(document.getElementById('openapi-spec').textContent),
 dom_id: '#swagger-ui',
 deepLinking: true,
 filter: true,
 displayOperationId: true,
 docExpansion: 'list',
 defaultModelsExpandDepth: 1,
 showExtensions: true,
 supportedSubmitMethods: [],
 tryItOutEnabled: false,
 validatorUrl: null,
 persistAuthorization: false,
 presets: [SwaggerUIBundle.presets.apis],
 layout: 'BaseLayout'
});
</script>
</body>
</html>
'''


def on_post_build(config):
    docs = Path(config['docs_dir'])
    prefix = Path('published') if (docs / 'published/05_api/openapi.yaml').is_file() else Path()
    target = Path(config['site_dir']) / prefix / 'assets/swagger/index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render(docs / prefix / '05_api/openapi.yaml'), encoding='utf-8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Verify generated source viewer without writing')
    args = parser.parse_args()
    expected = render(SPEC)
    if args.check:
        if not VIEWER.is_file() or VIEWER.read_text(encoding='utf-8') != expected:
            raise SystemExit('Swagger UI is stale. Run: python scripts/swagger_ui.py')
        print('Swagger UI matches the canonical UTF-8 OpenAPI YAML')
    else:
        VIEWER.parent.mkdir(parents=True, exist_ok=True)
        VIEWER.write_text(expected, encoding='utf-8')
        print('Generated:', VIEWER.relative_to(ROOT))
