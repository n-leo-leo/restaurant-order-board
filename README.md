# restaurant-order-board
Проектная работа: приложение для заказа и табло автоматизированного ресторана

Документация онлайн: https://n-leo-leo.github.io/restaurant-order-board/

## Структура репозитория

- `docs/home_work/` — выполненные домашние задания (исходные материалы)
- `docs/project/00_Описание_ДЗ.md` — требования к проектной работе
- `docs/project/01_План_проектной_работы.md` — план и чек-лист работ
- `docs/project/documentation/` — проектная документация (MkDocs)
- `mkdocs.yml` — настройки сайта документации

## Как открыть документацию локально

Первый запуск (один раз): создать виртуальное окружение и установить MkDocs.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Дальше каждый раз:

```bash
source .venv/bin/activate
mkdocs serve
```

Сайт откроется по адресу http://127.0.0.1:8000. Изменения в `.md` файлах видны сразу после сохранения. Остановить — `Ctrl+C`.

Собрать статический сайт: `mkdocs build` (результат в папке `site/`).

Если `python3` не найден, macOS предложит установить Command Line Tools — согласиться, затем повторить команды.

На GitHub сайт собирается автоматически при каждом push в `main` (`.github/workflows/docs.yml`).
