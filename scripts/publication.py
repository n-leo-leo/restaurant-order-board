"""Assemble public documentation from the project and pinned homework results."""
import atexit
import hashlib
import json
from html import escape
from pathlib import Path
import shutil
from tempfile import TemporaryDirectory
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]


def on_config(config):
    temporary = TemporaryDirectory(prefix='restaurant-docs-')
    atexit.register(temporary.cleanup)
    public = Path(temporary.name)
    shutil.copytree(ROOT / 'docs/project/published', public, dirs_exist_ok=True)
    assignments = json.loads((ROOT / 'scripts/homework-publication.json').read_text())
    homework_nav = [{'Принятые работы': 'homework/index.md'}]
    catalog = ['# Принятые домашние задания', '',
               'Принятые домашние задания по курсу «Системный аналитик». '
               'В [проектной работе](../index.md) некоторые решения доработаны.', '',
               'В этом разделе — только выполненные работы, без заданий и материалов курса.', '']
    for assignment in assignments:
        folder = assignment['folder']
        number, title = folder.split('. ', 1)
        if number == '17':
            raise ValueError('ДЗ 17 запрещено публиковать')
        target = public / 'homework' / number
        target.mkdir(parents=True)
        page = [f'# ДЗ {number}. {title}', '']
        downloads = []
        has_markdown = any(Path(entry['path']).suffix == '.md' for entry in assignment['files'])
        for entry in assignment['files']:
            relative = Path(entry['path'])
            source = ROOT / 'docs/home_work' / folder / relative
            if hashlib.sha256(source.read_bytes()).hexdigest() != entry['sha256']:
                raise ValueError(f'Принятая версия изменена: {source}. Проверьте результат перед обновлением публикации.')
            destination = target / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
            if '.assets' in relative.parts[0]:
                continue
            url = quote(relative.as_posix())
            extension = relative.suffix.lower()
            if extension == '.md':
                # Keep an exact source download; render the same text on the assignment page.
                raw = target / 'originals' / relative
                raw.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, raw.with_suffix('.txt'))
                downloads.append(f'- [{relative.name}](originals/{quote(relative.with_suffix(".txt").as_posix())})')
                page.extend(['', source.read_text(encoding='utf-8'), ''])
            else:
                downloads.append(f'- [{relative.name}]({url})')
                if extension in {'.png', '.jpeg', '.jpg'}:
                    page.extend(['', f'![{title}]({url})', ''])
                elif extension == '.pdf' and not has_markdown:
                    # The assignment index and its attachments share the same directory.
                    pdf_url = url
                    page.extend(['', f'<object data="{pdf_url}" type="application/pdf" '
                                 'width="100%" height="800" aria-label="Результат домашнего задания">'
                                 f'<p>Просмотр PDF недоступен. <a href="{pdf_url}">Открыть PDF</a></p></object>', ''])
                elif extension in {'.txt', '.yaml', '.yml'}:
                    text = escape(source.read_text(encoding='utf-8'))
                    page.extend(['', f'<pre><code>{text}</code></pre>', ''])
        page.extend(['', '## Скачать файлы', '', *downloads])
        (target / 'index.md').write_text('\n'.join(page) + '\n')
        catalog.append(f'- [ДЗ {number}. {title}]({number}/index.md)')
        homework_nav.append({f'{number}. {title}': f'homework/{number}/index.md'})
    (public / 'homework/index.md').write_text('\n'.join(catalog) + '\n')
    config.docs_dir = str(public)
    config.nav = [{'Проектная документация': config.nav}, {'Домашние задания': homework_nav}]
    return config
