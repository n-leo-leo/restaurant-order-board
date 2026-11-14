"""Assemble public documentation from the project and pinned homework results."""
import atexit
import hashlib
import json
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
               'Результаты домашних заданий курса «Системный аналитик». '
               'Здесь сохранены принятые версии работ; они могут отличаться от текущих решений '
               'в [проектной документации](../index.md).', '',
               'Условия заданий, учебные примеры и презентации курса в этот раздел не входят.', '']
    for assignment in assignments:
        folder = assignment['folder']
        number, title = folder.split('. ', 1)
        if number == '17':
            raise ValueError('ДЗ 17 запрещено публиковать')
        target = public / 'homework' / number
        target.mkdir(parents=True)
        page = [f'# ДЗ {number}. {title}', '', '**Статус: принято.**', '',
                'Сохранённая версия результата домашнего задания.', '', '## Результат', '']
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
            page.append(f'- [{relative.name}]({url})')
            if relative.suffix.lower() in {'.png', '.jpeg', '.jpg'}:
                page.extend(['', f'![{title}]({url})', ''])
        (target / 'index.md').write_text('\n'.join(page) + '\n')
        catalog.append(f'- [ДЗ {number}. {title}]({number}/index.md)')
        homework_nav.append({f'{number}. {title}': f'homework/{number}/index.md'})
    (public / 'homework/index.md').write_text('\n'.join(catalog) + '\n')
    config.docs_dir = str(public)
    config.nav = [{'Проектная документация': config.nav}, {'Домашние задания': homework_nav}]
    return config
