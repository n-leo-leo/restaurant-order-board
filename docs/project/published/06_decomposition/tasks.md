# Задачи реализации

Задачи относятся к разработке приложения. Их наличие не означает выполненную реализацию. A — сервер или адаптер; B — интерфейс и его взаимодействие с сервером. Каждая задача включает проверку своего результата по [DoD](dor-dod.md). Связи с экранами, operationId, данными и компонентами приведены по US в [трассировке](../08_traceability.md). R1 — первый релиз.

Зависимость означает готовый контракт и проверяемый результат предшествующей задачи; независимые интерфейсы можно разрабатывать на согласованном имитаторе. Циклов между задачами нет. Внешние возможности проверяются до интеграционного допуска по [реестру](../04_architecture/integrations.md#verification).

Проверки задач перечислены в матрице. Общие задачи дополнительно связаны с НФТ.

## MVP

| ID | US / AC | Конкретный результат | Зависимости |
|---|---|---|---|
| <a id="t-01a"></a>T-01A | US-01; [AC-01.1](acceptance-criteria.md#ac-01-1), [AC-17.2](acceptance-criteria.md#ac-17-2), [AC-17.3](acceptance-criteria.md#ac-17-3) | Выдача меню текущего дня с версиями и категориями | Согласованные модель и контракт |
| <a id="t-01b"></a>T-01B | US-01; [AC-01.1](acceptance-criteria.md#ac-01-1), [AC-17.2](acceptance-criteria.md#ac-17-2), [AC-17.3](acceptance-criteria.md#ac-17-3) | K-01: новая сессия, категории, цены, пустое и недоступное меню | T-01A |
| <a id="t-02a"></a>T-02A | US-02; [AC-02.1](acceptance-criteria.md#ac-02-1), [AC-09.4](acceptance-criteria.md#ac-09-4) | Атомарный резерв, проверка свежести и годности, восстановление unknown и истечение 5 мин | T-01A |
| <a id="t-02b"></a>T-02B | US-02; [AC-02.1](acceptance-criteria.md#ac-02-1), [AC-09.4](acceptance-criteria.md#ac-09-4) | K-01/03: скрытие недоступного и пересчет перед оплатой | T-02A |
| <a id="t-03a"></a>T-03A | US-03; [AC-03.1](acceptance-criteria.md#ac-03-1) | Карточка с составом, весом, аллергенами и ценой из версии меню | T-01A, T-02A |
| <a id="t-03b"></a>T-03B | US-03; [AC-03.1](acceptance-criteria.md#ac-03-1) | K-02: карточка и добавление без редактирования состава | T-03A |
| <a id="t-04a"></a>T-04A | US-04; [AC-04.1](acceptance-criteria.md#ac-04-1) | Версионная замена корзины с серверной суммой и количеством | T-01A, T-02A |
| <a id="t-04b"></a>T-04B | US-04; [AC-04.1](acceptance-criteria.md#ac-04-1) | K-01/03: добавление и показ состава и суммы | T-04A |
| <a id="t-05a"></a>T-05A | US-05; [AC-05.1](acceptance-criteria.md#ac-05-1) | Проверка пустой корзины, количеств и аннулирование прежнего согласия | T-04A |
| <a id="t-05b"></a>T-05B | US-05; [AC-05.1](acceptance-criteria.md#ac-05-1) | K-03: изменение, удаление и перечитывание при 412 | T-05A |
| <a id="t-06a"></a>T-06A | US-06; [AC-06.1](acceptance-criteria.md#ac-06-1) | Сохранение обязательного fulfillmentType в корзине и снимке | T-04A |
| <a id="t-06b"></a>T-06B | US-06; [AC-06.1](acceptance-criteria.md#ac-06-1) | K-03: выбор типа и передача в подтвержденный расчет | T-06A |
| <a id="t-07a"></a>T-07A | US-07; [AC-07.1](acceptance-criteria.md#ac-07-1) | Выбор доступных картошки и пирожка при бургере | T-02A, T-04A |
| <a id="t-07b"></a>T-07B | US-07; [AC-07.1](acceptance-criteria.md#ac-07-1) | K-02: предложение, отказ и добровольное добавление | T-07A |
| <a id="t-08a"></a>T-08A | US-08; [AC-08.1](acceptance-criteria.md#ac-08-1) | Расчет 10% по A-01 с временными границами и округлением | T-04A, T-06A |
| <a id="t-08b"></a>T-08B | US-08; [AC-08.1](acceptance-criteria.md#ac-08-1) | K-03: скидка, новый итог и явное согласие на calculationId | T-08A |
| <a id="t-09a"></a>T-09A | US-09; [AC-09.1](acceptance-criteria.md#ac-09-1), [AC-09.2](acceptance-criteria.md#ac-09-2), [AC-09.3](acceptance-criteria.md#ac-09-3), [AC-17.2](acceptance-criteria.md#ac-17-2), [AC-17.3](acceptance-criteria.md#ac-17-3), [AC-09.4](acceptance-criteria.md#ac-09-4), [AC-17.4](acceptance-criteria.md#ac-17-4) | Снимок до банка, попытка и транзакционная фиксация успеха, номера и доставок | T-02A, T-05A, T-06A, T-08A |
| <a id="t-09b"></a>T-09B | US-09; [AC-09.1](acceptance-criteria.md#ac-09-1), [AC-09.2](acceptance-criteria.md#ac-09-2), [AC-09.3](acceptance-criteria.md#ac-09-3), [AC-17.2](acceptance-criteria.md#ac-17-2), [AC-17.3](acceptance-criteria.md#ac-17-3), [AC-09.4](acceptance-criteria.md#ac-09-4), [AC-17.4](acceptance-criteria.md#ac-17-4) | K-03–06: запуск, восстановление activePurchaseId и проверенная копия талона | T-09A, T-15A |
| <a id="t-10a"></a>T-10A | US-10; [AC-09.2](acceptance-criteria.md#ac-09-2), [AC-10.1](acceptance-criteria.md#ac-10-1), [AC-17.2](acceptance-criteria.md#ac-17-2), [AC-09.4](acceptance-criteria.md#ac-09-4), [AC-17.4](acceptance-criteria.md#ac-17-4) | Сверка attemptId каждые 10 с, удержание резерва и проблема через 1 мин | T-09A |
| <a id="t-10b"></a>T-10B | US-10; [AC-09.2](acceptance-criteria.md#ac-09-2), [AC-10.1](acceptance-criteria.md#ac-10-1), [AC-17.2](acceptance-criteria.md#ac-17-2), [AC-09.4](acceptance-criteria.md#ac-09-4), [AC-17.4](acceptance-criteria.md#ac-17-4) | K-04: unknown, блокировка повторной оплаты и восстановление результата | T-10A |
| <a id="t-11a"></a>T-11A | US-11; [AC-11.1](acceptance-criteria.md#ac-11-1) | Проекция табло, подтверждение показа версии и применение исходного expiresAt | T-09A |
| <a id="t-11b"></a>T-11B | US-11; [AC-11.1](acceptance-criteria.md#ac-11-1) | B-01: две колонки, первый показ и восстановление подтверждения | T-11A |
| <a id="t-12a"></a>T-12A | US-12; [AC-09.3](acceptance-criteria.md#ac-09-3), [AC-12.1](acceptance-criteria.md#ac-12-1), [AC-16.2](acceptance-criteria.md#ac-16-2), [AC-16.4](acceptance-criteria.md#ac-16-4), [AC-16.5](acceptance-criteria.md#ac-16-5), [AC-16.6](acceptance-criteria.md#ac-16-6) | Адаптер талона и версионный цикл размещение/открытие/закрытие/пустота | T-11A |
| <a id="t-12b"></a>T-12B | US-12; [AC-09.3](acceptance-criteria.md#ac-09-3), [AC-12.1](acceptance-criteria.md#ac-12-1), [AC-16.2](acceptance-criteria.md#ac-16-2), [AC-16.4](acceptance-criteria.md#ac-16-4), [AC-16.5](acceptance-criteria.md#ac-16-5), [AC-16.6](acceptance-criteria.md#ac-16-6) | B-02: свой/чужой/истекший талон и подтвержденное завершение | T-12A |
| <a id="t-13a"></a>T-13A | US-13; [AC-13.1](acceptance-criteria.md#ac-13-1) | Скрытие проблемного номера на табло без раскрытия данных покупки и кода | T-11A |
| <a id="t-13b"></a>T-13B | US-13; [AC-13.1](acceptance-criteria.md#ac-13-1) | K-06 и B-01/02: постоянная подсказка о помощи | T-13A |
| <a id="t-14a"></a>T-14A | US-14; [AC-09.3](acceptance-criteria.md#ac-09-3), [AC-14.1](acceptance-criteria.md#ac-14-1), [AC-17.2](acceptance-criteria.md#ac-17-2), [AC-17.3](acceptance-criteria.md#ac-17-3), [AC-17.4](acceptance-criteria.md#ac-17-4) | Личные сессии сотрудников, назначение проблемы и запрет подмены внешних фактов | T-09A |
| <a id="t-14b"></a>T-14B | US-14; [AC-09.3](acceptance-criteria.md#ac-09-3), [AC-14.1](acceptance-criteria.md#ac-14-1), [AC-17.2](acceptance-criteria.md#ac-17-2), [AC-17.3](acceptance-criteria.md#ac-17-3), [AC-17.4](acceptance-criteria.md#ac-17-4) | S-00/01/02: звук, принятие, восстановление после потери ответа | T-14A |
| <a id="t-15a"></a>T-15A | US-15; [AC-09.3](acceptance-criteria.md#ac-09-3), [AC-15.1](acceptance-criteria.md#ac-15-1), [AC-09.4](acceptance-criteria.md#ac-09-4) | Точный поиск, проверка покупки, невозможность выполнения и сверка внешнего возврата | T-09A, T-14A |
| <a id="t-15b"></a>T-15B | US-15; [AC-09.3](acceptance-criteria.md#ac-09-3), [AC-15.1](acceptance-criteria.md#ac-15-1), [AC-09.4](acceptance-criteria.md#ac-09-4) | S-02: исходная покупка, проверенная печать и раздельные деньги/документы | T-15A |
| <a id="t-16a"></a>T-16A | US-16; [AC-16.1](acceptance-criteria.md#ac-16-1), [AC-16.2](acceptance-criteria.md#ac-16-2), [AC-16.3](acceptance-criteria.md#ac-16-3), [AC-16.4](acceptance-criteria.md#ac-16-4), [AC-16.5](acceptance-criteria.md#ac-16-5), [AC-16.6](acceptance-criteria.md#ac-16-6) | Исходный срок, частичная выдача, неявка, неисправность и контроль уборки | T-12A, T-14A |
| <a id="t-16b"></a>T-16B | US-16; [AC-16.1](acceptance-criteria.md#ac-16-1), [AC-16.2](acceptance-criteria.md#ac-16-2), [AC-16.3](acceptance-criteria.md#ac-16-3), [AC-16.4](acceptance-criteria.md#ac-16-4), [AC-16.5](acceptance-criteria.md#ac-16-5), [AC-16.6](acceptance-criteria.md#ac-16-6) | S-03: обслуживание с проверкой закрытия, исправности и пустоты | T-16A |
| <a id="t-17a"></a>T-17A | US-17; [AC-17.1](acceptance-criteria.md#ac-17-1), [AC-17.2](acceptance-criteria.md#ac-17-2), [AC-17.3](acceptance-criteria.md#ac-17-3), [AC-17.4](acceptance-criteria.md#ac-17-4) | Очистка 2+2 мин, блокировка активной оплаты, порядок stop/start и торгового дня | T-09A, T-10A, T-14A |
| <a id="t-17b"></a>T-17B | US-17; [AC-17.1](acceptance-criteria.md#ac-17-1), [AC-17.2](acceptance-criteria.md#ac-17-2), [AC-17.3](acceptance-criteria.md#ac-17-3), [AC-17.4](acceptance-criteria.md#ac-17-4) | K-07/S-04: остановка, проверки перед resume и безопасное завершение | T-17A |
| <a id="t-35a"></a>T-35A | US-35; [AC-35.1](acceptance-criteria.md#ac-35-1) | Задачи фискализации и печати по исходным ID и сверка unknown | T-09A, T-14A |
| <a id="t-35b"></a>T-35B | US-35; [AC-35.1](acceptance-criteria.md#ac-35-1) | K-05/06, S-02: раздельные статусы чека, талона и передачи помощи | T-35A |

## R1

| ID | US / AC | Конкретный результат | Зависимости |
|---|---|---|---|
| <a id="t-18a"></a>T-18A | US-18; [AC-18.1](acceptance-criteria.md#ac-18-1) | Адаптер SMS и создание одного профиля с сохранением корзины | T-04A |
| <a id="t-18b"></a>T-18B | US-18; [AC-18.1](acceptance-criteria.md#ac-18-1) | R-01: регистрация, обязательные данные и Retry-After | T-18A |
| <a id="t-19a"></a>T-19A | US-19; [AC-19.1](acceptance-criteria.md#ac-19-1) | Вход одноразовым кодом и получение баланса только своего счета | T-18A |
| <a id="t-19b"></a>T-19B | US-19; [AC-19.1](acceptance-criteria.md#ac-19-1) | R-01/02: вход, баланс и недоступность лояльности | T-19A |
| <a id="t-20a"></a>T-20A | US-20; [AC-20.1](acceptance-criteria.md#ac-20-1) | Резерв/списание бонусов с лимитом 30%, сверкой и компенсацией | T-08A, T-19A |
| <a id="t-20b"></a>T-20B | US-20; [AC-20.1](acceptance-criteria.md#ac-20-1) | R-02: выбор бонусов, остаток и согласие при пересчете | T-20A |
| <a id="t-21a"></a>T-21A | US-21; [AC-21.1](acceptance-criteria.md#ac-21-1) | Однократное начисление 5% денежной оплаты и отмена начисления | T-09A, T-20A |
| <a id="t-21b"></a>T-21B | US-21; [AC-21.1](acceptance-criteria.md#ac-21-1) | R-02/K-05: результат бонусов без блокировки подтвержденной покупки | T-21A |
| <a id="t-22a"></a>T-22A | US-22; [AC-22.1](acceptance-criteria.md#ac-22-1) | Адаптер наличных: взнос, сдача, отмена неполной суммы и сверка | T-09A, T-10A |
| <a id="t-22b"></a>T-22B | US-22; [AC-22.1](acceptance-criteria.md#ac-22-1) | R-03: выбор исправного способа, внесено, сдача и неизвестный возврат | T-22A |
| <a id="t-23a"></a>T-23A | US-23; [AC-23.1](acceptance-criteria.md#ac-23-1) | Фильтры поиска по периоду, оплате и состоянию в пределах прав ресторана | T-15A |
| <a id="t-23b"></a>T-23B | US-23; [AC-23.1](acceptance-criteria.md#ac-23-1) | R-04: список, пустой результат и карточка с возвратами | T-23A |
| <a id="t-24a"></a>T-24A | US-24; [AC-24.1](acceptance-criteria.md#ac-24-1) | Отмена по A-12 и запуск полного карточного возврата с постоянным ID | T-15A, T-23A |
| <a id="t-24b"></a>T-24B | US-24; [AC-24.1](acceptance-criteria.md#ac-24-1) | R-04: отдельные результаты отмены, денег и кассового документа | T-24A |
| <a id="t-25a"></a>T-25A | US-25; [AC-25.1](acceptance-criteria.md#ac-25-1) | Наличный возврат с подтверждением выдачи, аудитом и защитой от дубля | T-22A, T-24A |
| <a id="t-25b"></a>T-25B | US-25; [AC-25.1](acceptance-criteria.md#ac-25-1) | R-04: отмена и регистрация полного наличного возврата | T-25A |
| <a id="t-26a"></a>T-26A | US-26; [AC-26.1](acceptance-criteria.md#ac-26-1) | Проекция уведомлений о снятии блюд и сбоях с дедупликацией | T-14A, T-23A |
| <a id="t-26b"></a>T-26B | US-26; [AC-26.1](acceptance-criteria.md#ac-26-1) | R-04: тип, время, описание и затронутые заказы | T-26A |
| <a id="t-27a"></a>T-27A | US-27; [AC-27.1](acceptance-criteria.md#ac-27-1) | Версионное сохранение позиции только в меню следующего дня | T-01A, T-14A |
| <a id="t-27b"></a>T-27B | US-27; [AC-27.1](acceptance-criteria.md#ac-27-1) | R-05: добавление, обязательные поля и конфликт 412 | T-27A |
| <a id="t-28a"></a>T-28A | US-28; [AC-28.1](acceptance-criteria.md#ac-28-1) | Цена в будущей версии меню без изменения оплаченных снимков | T-27A |
| <a id="t-28b"></a>T-28B | US-28; [AC-28.1](acceptance-criteria.md#ac-28-1) | R-05: изменение цены, валидация и дата применения | T-28A |
| <a id="t-29a"></a>T-29A | US-29; [AC-29.1](acceptance-criteria.md#ac-29-1) | Будущие правила акций и наборы из готовых блюд | T-08A, T-27A |
| <a id="t-29b"></a>T-29B | US-29; [AC-29.1](acceptance-criteria.md#ac-29-1) | R-05: период, состав комбо, валидация и конфликт версии | T-29A |
| <a id="t-30a"></a>T-30A | US-30; [AC-30.1](acceptance-criteria.md#ac-30-1) | Версия техкарты с IngredientRef, количествами и параметрами | T-27A |
| <a id="t-30b"></a>T-30B | US-30; [AC-30.1](acceptance-criteria.md#ac-30-1) | R-06: выбор блюда, ингредиентов, проверка и сохранение будущей версии | T-30A |
| <a id="t-31a"></a>T-31A | US-31; [AC-31.1](acceptance-criteria.md#ac-31-1) | Порог подарка после скидок до бонусов и атомарный резерв стакана | T-02A, T-20A, T-29A |
| <a id="t-31b"></a>T-31B | US-31; [AC-31.1](acceptance-criteria.md#ac-31-1) | R-02/05: подарок, отсутствие и новое согласие при изменении | T-31A |
| <a id="t-32a"></a>T-32A | US-32; [AC-32.1](acceptance-criteria.md#ac-32-1) | Чтение всех роботов, ошибок и asOf из I-03 | T-14A |
| <a id="t-32b"></a>T-32B | US-32; [AC-32.1](acceptance-criteria.md#ac-32-1) | R-07: обновление не реже 30 с и признак устаревания | T-32A |
| <a id="t-33a"></a>T-33A | US-33; [AC-33.1](acceptance-criteria.md#ac-33-1) | Остатки с единицами, порог ниже 30% и оценка окончания | T-32A |
| <a id="t-33b"></a>T-33B | US-33; [AC-33.1](acceptance-criteria.md#ac-33-1) | R-07: потребность пополнения и устаревшие данные | T-33A |
| <a id="t-34a"></a>T-34A | US-34; [AC-34.1](acceptance-criteria.md#ac-34-1) | Отчет A-13 за [from,to), пакет закрытого дня и постоянные ID строк 1С | T-09A, T-15A, T-23A |
| <a id="t-34b"></a>T-34B | US-34; [AC-34.1](acceptance-criteria.md#ac-34-1) | R-08: сверка итога, статус и повтор исходного пакета при сбое | T-34A |

## Общие задачи

Зависимости указывают на конкретные задачи. Зависимость интерфейса от серверной задачи допускает разработку на согласованном имитаторе; завершение требует проверки вместе. Все задачи ниже входят в реализацию или приемку перечисленных историй.

| ID | Релиз | US / AC | НФТ | Результат | Зависимости | Проверки |
|---|---|---|---|---|---|---|
| <a id="t-n01"></a>T-N01 | MVP | US-01, US-02, US-09, US-11; [AC-01.1](acceptance-criteria.md#ac-01-1), [AC-02.1](acceptance-criteria.md#ac-02-1), [AC-09.1](acceptance-criteria.md#ac-09-1), [AC-09.4](acceptance-criteria.md#ac-09-4), [AC-11.1](acceptance-criteria.md#ac-11-1) | НФТ-01, НФТ-02, НФТ-03, НФТ-08 | Метрики событий оплаты/отправки и обновлений меню/табло; генератор профилей 4 киосков, 10/130 ресторанов и отчет сверки | T-09A, T-11A | TC-N01, TC-N02, TC-N07, TC-M18 |
| <a id="t-n02"></a>T-N02 | MVP | US-01, US-09, US-10, US-14, US-17; [AC-09.2](acceptance-criteria.md#ac-09-2), [AC-17.3](acceptance-criteria.md#ac-17-3) | НФТ-04, НФТ-05, НФТ-06, НФТ-07 | Транзакционная доставка, восстановление обработчиков и БД, ежедневные копии/WAL, регламент восстановления и расчет доступности | T-09A, T-17A | TC-N03, TC-N04, TC-N05, TC-N06 |
| <a id="t-n03"></a>T-N03 | MVP | US-01, US-09, US-10, US-14, US-17; [AC-09.1](acceptance-criteria.md#ac-09-1), [AC-10.1](acceptance-criteria.md#ac-10-1), [AC-17.2](acceptance-criteria.md#ac-17-2), [AC-17.3](acceptance-criteria.md#ac-17-3) | НФТ-09, НФТ-10 | Проверки обязательных зависимостей, сверка внешних ID и защищенные от дублей доставки; наблюдаемые причины блокировки | T-09A, T-10A, T-17A | TC-N08, TC-N09 |
| <a id="t-n04"></a>T-N04 | MVP | US-01, US-05, US-06, US-09; [AC-01.1](acceptance-criteria.md#ac-01-1), [AC-05.1](acceptance-criteria.md#ac-05-1), [AC-06.1](acceptance-criteria.md#ac-06-1), [AC-09.1](acceptance-criteria.md#ac-09-1) | НФТ-11 | Сценарий исследования с 10 участниками, измерение времени и отчет о завершениях и медиане для приемки интерфейса | T-01B, T-05B, T-06B, T-09B | TC-N10 |
| <a id="t-n05"></a>T-N05 | MVP | US-09, US-10, US-12, US-14, US-15, US-16, US-17; [AC-09.1](acceptance-criteria.md#ac-09-1), [AC-09.3](acceptance-criteria.md#ac-09-3), [AC-14.1](acceptance-criteria.md#ac-14-1), [AC-15.1](acceptance-criteria.md#ac-15-1), [AC-16.3](acceptance-criteria.md#ac-16-3), [AC-17.1](acceptance-criteria.md#ac-17-1), [AC-17.4](acceptance-criteria.md#ac-17-4) | НФТ-12, НФТ-13, НФТ-14, НФТ-15, НФТ-16 | Проверка ролей/ресторана на сервере, защищенные каналы, очистка сессии и журнал с регламентом 90 дней без удаления бизнесовых ключей | T-14A, T-15A, T-17A | TC-N11, TC-N12, TC-N13, TC-N14, TC-N15 |
| <a id="t-n06"></a>T-N06 | MVP | US-09, US-11, US-12, US-16; [AC-09.1](acceptance-criteria.md#ac-09-1), [AC-11.1](acceptance-criteria.md#ac-11-1), [AC-12.1](acceptance-criteria.md#ac-12-1), [AC-16.1](acceptance-criteria.md#ac-16-1), [AC-16.2](acceptance-criteria.md#ac-16-2), [AC-16.3](acceptance-criteria.md#ac-16-3), [AC-16.4](acceptance-criteria.md#ac-16-4), [AC-16.5](acceptance-criteria.md#ac-16-5), [AC-16.6](acceptance-criteria.md#ac-16-6) | НФТ-17, НФТ-20 | Конфигурация согласованного оборудования, контрактные наборы I-01–05, параметры контроля ячейки и протокол совместимости | T-12A, T-16A | TC-N16, TC-N20 |
| <a id="t-n07"></a>T-N07 | MVP | US-14; [AC-14.1](acceptance-criteria.md#ac-14-1) | НФТ-19 | Метки доставки/принятия проблемы и регламент дежурства менеджера; отчет о реакции за минуту | T-14A, T-14B | TC-N19 |
| <a id="t-n08"></a>T-N08 | R1 | US-18, US-19, US-20, US-27, US-30, US-32, US-33, US-34; [AC-18.1](acceptance-criteria.md#ac-18-1), [AC-19.1](acceptance-criteria.md#ac-19-1), [AC-20.1](acceptance-criteria.md#ac-20-1), [AC-27.1](acceptance-criteria.md#ac-27-1), [AC-30.1](acceptance-criteria.md#ac-30-1), [AC-32.1](acceptance-criteria.md#ac-32-1), [AC-33.1](acceptance-criteria.md#ac-33-1), [AC-34.1](acceptance-criteria.md#ac-34-1) | НФТ-12, НФТ-14, НФТ-15, НФТ-16, НФТ-18 | Регламент обезличивания профиля через 12 месяцев, роли R1 и изоляция лояльности; контроль asOf производства 30 с | T-N05, T-18A, T-32A | TC-R35, TC-R36, TC-R37, TC-R42, TC-R43, TC-R53 |
