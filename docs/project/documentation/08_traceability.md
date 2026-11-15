# Матрица трассировки

Связи БТ → US → AC дополнены экранами и operationId этапа 3. Сущности, компоненты и интеграции приведены ниже. Задачи, DoR/DoD и тест-кейсы завершаются на этапе 4.

| Бизнес-требование | US | Черновой AC | Задача | API (operationId) | Тест-кейс |
|---|---|---|---|---|---|
| БТ-01 | US-01 | AC-01.1 | Этап 4 | startSession, getMenu | Этап 4 |
| БТ-04 | US-02 | AC-02.1 | Этап 4 | getMenu, preparePurchase | Этап 4 |
| БТ-01, БТ-02 | US-03 | AC-03.1 | Этап 4 | getMenuItem | Этап 4 |
| БТ-01 | US-04 | AC-04.1 | Этап 4 | getCart, replaceCart | Этап 4 |
| БТ-01 | US-05 | AC-05.1 | Этап 4 | replaceCart | Этап 4 |
| БТ-01 | US-06 | AC-06.1 | Этап 4 | replaceCart, startPayment | Этап 4 |
| БТ-14 | US-07 | AC-07.1 | Этап 4 | getMenuItem, replaceCart | Этап 4 |
| БТ-15 | US-08 | AC-08.1 | Этап 4 | preparePurchase | Этап 4 |
| БТ-03, БТ-05 | US-09 | AC-09.1 | Этап 4 | preparePurchase, startPayment, getPayment, getPurchase, verifyPurchase, reprintTicket | Этап 4 |
| БТ-03, БТ-07 | US-10 | AC-10.1 | Этап 4 | getPayment, getPurchase | Этап 4 |
| БТ-06 | US-11 | AC-11.1 | Этап 4 | getBoard, confirmBoardDisplay, getBoardDisplay | Этап 4 |
| БТ-06 | US-12 | AC-12.1 | Этап 4 | I-03 (талон и выдача), reprintTicket | Этап 4 |
| БТ-07 | US-13 | AC-13.1 | Этап 4 | getPurchase, getBoard; помощь в зале | Этап 4 |
| БТ-07 | US-14 | AC-14.1 | Этап 4 | listProblems, acceptProblem, resolveProblem, getStaffSalesState, setSalesState | Этап 4 |
| БТ-07, БТ-10 | US-15 | AC-15.1 | Этап 4 | findPurchases, getStaffPurchase, recordImpossibility, registerExternalRefund, getRefund | Этап 4 |
| БТ-06, БТ-07 | US-16 | AC-16.1 | Этап 4 | listCells, serviceCell, acceptProblem | Этап 4 |
| БТ-01, БТ-02 | US-17 | AC-17.1 | Этап 4 | endSession, getSession, getSalesState, setSalesState | Этап 4 |
| БТ-08 | US-18 | AC-18.1 | Этап 4 | requestLoyaltyCode, confirmLoyalty | Этап 4 |
| БТ-08 | US-19 | AC-19.1 | Этап 4 | confirmLoyalty, getLoyalty | Этап 4 |
| БТ-08 | US-20 | AC-20.1 | Этап 4 | getLoyalty, preparePurchase | Этап 4 |
| БТ-08 | US-21 | AC-21.1 | Этап 4 | getPurchase; I-07 начисление по оплате | Этап 4 |
| БТ-09 | US-22 | AC-22.1 | Этап 4 | startPayment, getPayment, cancelCashPayment | Этап 4 |
| БТ-07, БТ-10 | US-23 | AC-23.1 | Этап 4 | findPurchases, getStaffPurchase | Этап 4 |
| БТ-10 | US-24 | AC-24.1 | Этап 4 | cancelOrder, startRefund, getRefund | Этап 4 |
| БТ-10 | US-25 | AC-25.1 | Этап 4 | cancelOrder, startRefund, registerExternalRefund, getRefund | Этап 4 |
| БТ-07 | US-26 | AC-26.1 | Этап 4 | listNotifications | Этап 4 |
| БТ-11 | US-27 | AC-27.1 | Этап 4 | getMenuDraft, saveMenuEntry | Этап 4 |
| БТ-11 | US-28 | AC-28.1 | Этап 4 | getMenuDraft, saveMenuEntry | Этап 4 |
| БТ-11 | US-29 | AC-29.1 | Этап 4 | savePromotion, saveMenuEntry | Этап 4 |
| БТ-11 | US-30 | AC-30.1 | Этап 4 | getIngredients, getRecipe, saveRecipe | Этап 4 |
| БТ-16 | US-31 | AC-31.1 | Этап 4 | preparePurchase, savePromotion | Этап 4 |
| БТ-17 | US-32 | AC-32.1 | Этап 4 | getProduction | Этап 4 |
| БТ-17 | US-33 | AC-33.1 | Этап 4 | getProduction | Этап 4 |
| БТ-13 | US-34 | AC-34.1 | Этап 4 | getSalesReport, createExport, getExport | Этап 4 |
| БТ-18 | US-35 | AC-35.1 | Этап 4 | getPurchase, getStaffPurchase | Этап 4 |
| БТ-06, БТ-07 | US-12, US-16 | AC-16.2 | Этап 4 | I-03 (талон и выдача), reprintTicket, listCells, serviceCell, acceptProblem | Этап 4 |
| БТ-06, БТ-07 | US-16 | AC-16.3 | Этап 4 | listCells, serviceCell, acceptProblem | Этап 4 |
| БТ-03, БТ-05, БТ-07 | US-09, US-10 | AC-09.2 | Этап 4 | preparePurchase, startPayment, getPayment, getPurchase, verifyPurchase, reprintTicket | Этап 4 |
| БТ-03, БТ-06, БТ-07, БТ-10 | US-09, US-12, US-14, US-15 | AC-09.3 | Этап 4 | preparePurchase, startPayment, getPayment, getPurchase, verifyPurchase, reprintTicket, I-03 (талон и выдача), listProblems, acceptProblem, resolveProblem, getStaffSalesState, setSalesState, findPurchases, getStaffPurchase, recordImpossibility, registerExternalRefund, getRefund | Этап 4 |
| БТ-06, БТ-07 | US-12, US-16 | AC-16.4 | Этап 4 | I-03 (талон и выдача), reprintTicket, listCells, serviceCell, acceptProblem | Этап 4 |
| БТ-01, БТ-02, БТ-03, БТ-05, БТ-07 | US-01, US-09, US-10, US-14, US-17 | AC-17.2 | Этап 4 | startSession, getMenu, preparePurchase, startPayment, getPayment, getPurchase, verifyPurchase, reprintTicket, listProblems, acceptProblem, resolveProblem, getStaffSalesState, setSalesState, endSession, getSession, getSalesState | Этап 4 |
| БТ-01, БТ-02, БТ-03, БТ-05, БТ-07 | US-01, US-09, US-14, US-17 | AC-17.3 | Этап 4 | startSession, getMenu, preparePurchase, startPayment, getPayment, getPurchase, verifyPurchase, reprintTicket, listProblems, acceptProblem, resolveProblem, getStaffSalesState, setSalesState, endSession, getSession, getSalesState | Этап 4 |

## Требования без отдельной пользовательской истории

| Требование | Чем покрывается |
|---|---|
| БТ-02 — понятность интерфейса | US-03, US-13, US-17; НФТ-11 и будущая проверка удобства |
| БТ-05 — передача роботам | US-09; НФТ-02, НФТ-04; процесс приготовления |
| БТ-12 — поэтапность | Карта историй и разделение функций по релизам; отдельная функция приложения не требуется |

## Связи уточненных правил

| Правило | Процесс и проверка |
|---|---|
| A-07/A-08; НФТ-05/10 — сохранение покупки до оплаты | Оформление и оплата; US-09/10; AC-09.1/09.2 и AC-10.1; метрика М-08 |
| A-03/A-14 — помощь без талона | Оформление и помощь; US-09/12/14/15; AC-09.3 и AC-15.1; права и аудит — НФТ-12–15 |
| A-02/A-04 — остаток заказа после срока хранения | Приготовление и выдача; US-12/16; AC-16.2/16.4; НФТ-20 |
| A-10 — порог подарка после скидок, до бонусов | Управление меню и акции; БТ-16, US-31, AC-31.1 |
| A-15 — плановая остановка продаж | Оформление и оплата; US-01/09/10/14/17; AC-17.2/17.3; доступность — НФТ-04, изоляция сессий — НФТ-14, аудит — НФТ-15 |

Плановая остановка — операционный порядок для существующих историй, без отдельного календаря и изменения состава релизов.

## Цели и требования

| Цель | Связь |
|---|---|
| Ц-1 — проверка пилота | Метрики М-01–04, М-06–11; приемка требований MVP |
| Ц-2 — снижение издержек | БТ-01, БТ-03, БТ-05, БТ-06; эффект оценивается на уровне ресторана, а не одного приложения |
| Ц-3 — сокращение персонала | БТ-05, БТ-17; зависит от роботизированного комплекса |
| Ц-4 — автоматическое обслуживание | БТ-01–07 и соответствующие истории MVP |
| Ц-5 — тиражирование | НФТ-03; нагрузка и архитектура этапа 2 |

Количественные и организационные ограничения из раздела бизнеса проверяются расчетами и оценкой пилота, а не искусственными историями гостя. Технические зависимости проверяются на этапе 2; содержимое этапа 1 не считается согласованным только по одобрению структуры.

## Связи модели и архитектуры этапа 2

Имена сущностей соответствуют [диаграмме классов](../published/03_model/class-diagram.md) и [словарю](../published/03_model/entities.md). C-ID определены в [компонентах](../published/04_architecture/components.md), I-ID — в [интеграциях](../published/04_architecture/integrations.md). Состояния приведены в [модели переходов](../published/03_model/order-states.md). Релиз каждой истории сохраняется по карте.

| US | Сущности | Компоненты | Интеграции |
|---|---|---|---|
| US-01–03 | Restaurant, TradingDay, MenuVersion, MenuEntry, Dish, RecipeVersion, Session | C-01/02/08 | I-01 |
| US-04–05 | Cart, CartLine, Order, OrderLine | C-01/02 | I-01 перед оплатой |
| US-06 | Order.fulfillmentType, KitchenJob | C-02/05 | I-03 |
| US-07–08 | MenuEntry, PromotionRule, OrderLine | C-01/02 | I-01 |
| US-09–10 | Order, Reservation, PaymentAttempt, KitchenJob, Ticket, PrintTask | C-02–06/08 | I-01–05 |
| US-11–12 | KitchenJob, CellRef, CellAssignment, Ticket | C-05/08 | I-03/05 |
| US-13–14 | Problem, Notification, Employee, Role | C-05/07/08 | I-03 |
| US-15 | Order, Problem, Refund, PaymentAttempt, FiscalOperation | C-04/06/07 | I-02/04 |
| US-16 | CellRef, CellAssignment, Problem, Notification | C-05/07/08 | I-03 |
| US-17 | Session, Cart, Reservation, PaymentAttempt, Restaurant | C-02/03/04/08 | I-01/02 |
| US-18–19 | LoyaltyProfileRef, Session | C-07/09 | I-07/08 |
| US-20–21 | BonusOperationRef, Order, PaymentAttempt | C-02/04/09 | I-07 |
| US-22 | PaymentAttempt, Ticket, PrintTask | C-04/06 | I-04/05/10 |
| US-23 | Order, Problem, PaymentAttempt, Refund | C-02/04/07 | I-02/04 |
| US-24–25 | Order, Refund, KitchenJob, CellAssignment, FiscalOperation | C-04–07 | I-02/03/04/10 по способу |
| US-26 | Problem, Notification, MenuEntry | C-01/07 | I-01/03 |
| US-27–29 | MenuVersion, MenuEntry, PromotionRule, ComboLine, TradingDay | C-01/07/08 | — |
| US-30 | RecipeVersion, RecipeLine, IngredientRef | C-01/07 | I-01 — справочник IngredientRef; I-03 — согласованная версия |
| US-31 | GiftAllocation, Reservation, Order | C-02/03/09 | I-01/03 |
| US-32–33 | RobotRef, IngredientRef, актуальность состояний | C-05/07 | I-03; в MVP внешний I-06 |
| US-34 | Order, PaymentAttempt, Refund, ExportBatch, ExportLine | C-04/10 | I-09 |
| US-35 | FiscalOperation, PrintTask, Problem | C-06/07 | I-04/05 |

Группы диапазонов охватывают все US-01–35; они не меняют ID и не объединяют истории. AC-09.4 связан с US-02/09/10/15, AC-16.5/16.6 — с US-12/16, AC-17.4 — с US-09/10/14/17. Их БТ следуют из существующих связей этих историй.

| НФТ | Данные и компоненты | Проверка |
|---|---|---|
| НФТ-01–03 | C-01–06/08, снимки, задания и проекции | Профиль нагрузки, 4 киоска, сеть 10–130, первая отправка ≤1 с для подтвержденного пригодного резерва, включая проверку; неизвестная пригодность — сверка, невозможность исполнения — полный возврат |
| НФТ-04–07 | C-08, PostgreSQL, копии и WAL | Бюджет A-16, резервирование, RPO/RTO и восстановление |
| НФТ-08–10 | C-01/03/04/05/08, версии и ID операций | Свежесть p95 ≤2 с, блокировка, внешние повторы и сверка |
| НФТ-11 | C-01/02, Session | 10 представителей, медиана ≤3 мин; среднее отдельно для мощности |
| НФТ-12–16 | C-07/08/09, роли, сессии, аудит, профиль | Права по ресторану, очистка, отсутствие карточных данных, 90 дней/12 месяцев |
| НФТ-17 | Адаптеры C-03–06/09/10 | REST, совместимость оборудования, инфраструктура заказчика |
| НФТ-18 | C-05, RobotRef | Первый релиз, обновление не реже 30 с и признак устаревания |
| НФТ-19 | C-07, Notification | Доставка и принятие ≤1 мин |
| НФТ-20 | C-05, CellAssignment, Ticket, I-03 | Последовательность веса/дверцы, остатки, срок, неисправность; подтверждение первого показа и применения expiresAt — AC-11.1 |

A-16 связан с НФТ-04/М-07, AC-17.3 и расчетом доступности. Регулярные технические работы выполняются вне 10:00–22:00; остановки внутри дня по A-15 суммируются со сбоями в общем бюджете простоя. A-02/A-03/A-05/A-08/A-14 связаны с реестром проверок внешних возможностей. Расчетный профиль и испытания A-06 находятся в [нагрузке](../published/04_architecture/load-db.md#verification). Подтверждение конкретных поставщиков не получено; связи не означают успешного испытания.

## Цепочки интерфейсов и API этапа 3

[Описание экранов](../published/05_api/ui.md), [полноразмерные прототипы](../published/05_api/prototypes.md), [операции](../published/05_api/resources.md), [схемы данных OpenAPI](../published/05_api/openapi.yaml) и [последовательности](../published/04_architecture/integration-flows.md) образуют продолжение архитектурной матрицы выше. AC каждой истории перечислены в основной таблице; дополнительные AC сохранены со своими ID.

| US | Экран | Операция / внешний интерфейс |
|---|---|---|
| US-01 | K-01 | startSession, getMenu |
| US-02 | K-01/03 | getMenu, preparePurchase |
| US-03 | K-02 | getMenuItem |
| US-04 | K-01/03 | getCart, replaceCart |
| US-05 | K-03 | replaceCart |
| US-06 | K-03 | replaceCart, startPayment |
| US-07 | K-02 | getMenuItem, replaceCart |
| US-08 | K-03 | preparePurchase |
| US-09 | K-03–06, S-02 | preparePurchase, startPayment, getPayment, getPurchase, verifyPurchase, reprintTicket |
| US-10 | K-04/06 | getPayment, getPurchase |
| US-11 | B-01 | getBoard, confirmBoardDisplay, getBoardDisplay |
| US-12 | B-02, S-02 | I-03 (талон и выдача), reprintTicket |
| US-13 | K-06, B-01/02 | getPurchase, getBoard; помощь в зале |
| US-14 | S-01/02/04 | listProblems, acceptProblem, resolveProblem, getStaffSalesState, setSalesState |
| US-15 | S-01/02 | findPurchases, getStaffPurchase, recordImpossibility, registerExternalRefund, getRefund |
| US-16 | S-03 | listCells, serviceCell, acceptProblem |
| US-17 | K-01/07, S-04 | endSession, getSession, getSalesState, setSalesState |
| US-18 | R-01 | requestLoyaltyCode, confirmLoyalty |
| US-19 | R-01/02 | confirmLoyalty, getLoyalty |
| US-20 | R-02 | getLoyalty, preparePurchase |
| US-21 | R-02, K-05 | getPurchase; I-07 начисление по оплате |
| US-22 | R-03 | startPayment, getPayment, cancelCashPayment |
| US-23 | R-04 | findPurchases, getStaffPurchase |
| US-24 | R-04 | cancelOrder, startRefund, getRefund |
| US-25 | R-04 | cancelOrder, startRefund, registerExternalRefund, getRefund |
| US-26 | R-04 | listNotifications |
| US-27 | R-05 | getMenuDraft, saveMenuEntry |
| US-28 | R-05 | getMenuDraft, saveMenuEntry |
| US-29 | R-05 | savePromotion, saveMenuEntry |
| US-30 | R-06 | getMenuDraft, getIngredients, getRecipe, saveRecipe |
| US-31 | R-02/05 | preparePurchase, savePromotion |
| US-32 | R-07 | getProduction |
| US-33 | R-07 | getProduction |
| US-34 | R-08 | getSalesReport, createExport, getExport |
| US-35 | K-05/06, S-02 | getPurchase, getStaffPurchase |

| Ветка и AC | Экран → операция | Данные/состояние → компонент/интеграция → результат и восстановление |
|---|---|---|
| Расчет и согласие, AC-05.1/08.1/09.1 | K-03 → replaceCart, preparePurchase, startPayment | Cart.version, Calculation, Reservation → C-01–04/I-01/02 → явное согласие, снимок до банка; конфликт требует перечитать |
| Неизвестный платеж, AC-09.2/09.4/10.1 | K-04 → getPayment, getPurchase | PaymentAttempt.unknown, исходный резерв → C-03/04/08/I-01/02 → сверка каждые 10 с, менеджер через 1 мин; поздний успех без новой покупки, непригодность — полный возврат |
| Документы и помощь, AC-09.3/15.1/35.1 | K-05/06, S-02 → getStaffPurchase, verifyPurchase, reprintTicket | FiscalOperation, PrintTask, Problem → C-06/07/I-04/05 → тот же талон, независимый чек, повтор исходной команды |
| Первое появление и доступ, AC-11.1/12.1 | B-01/02 → getBoard, confirmBoardDisplay, getBoardDisplay; I-03 | Версия проекции, CellAssignment.firstReadyAt/expiresAt → C-05/08/I-03 → 10 мин от первого показа; применение срока до доступа; сверка исходной версии |
| Частичное получение, срок и контроль, AC-16.1–16.6 | B-02/S-03 → I-03, listCells, serviceCell | CellAssignment, Ticket, исправность/последовательность → C-05/07/I-03 → issued только по полному циклу; остаток сохраняет срок, неявка/неисправность требует обслуживания |
| Отмена и деньги, AC-15.1/24.1/25.1 | S-02/R-04 → recordImpossibility, registerExternalRefund; R1 cancelOrder/startRefund | Order и Refund раздельно → C-04–07/I-02/03/04/10 → полный возврат по исходной операции; unknown не закрывается отметкой |
| Остановка и гонка, AC-17.2–17.4 | K-07/S-04 → getSalesState, setSalesState | Restaurant.manualStop, PaymentAttempt → C-02/04/08 → порядок регистрации, запрет только новых оплат; старые сверяются, resume после проверок |
| Лояльность и подарок, AC-18.1–21.1/31.1 | R-01/02 → confirmLoyalty, getLoyalty, preparePurchase | LoyaltyProfileRef, BonusOperationRef, GiftAllocation → C-02/03/09/I-01/07/08 → лимит 30%, начисление 5%, строгий порог подарка, компенсация при возврате |
| Наличные, AC-22.1 | R-03 → startPayment, getPayment, cancelCashPayment | PaymentAttempt, возврат внесенного → C-04/I-10 → подтверждение суммы, сдача; неизвестный возврат блокирует терминал |
| Рабочие места, AC-23.1/26.1–30.1/32.1–34.1 | R-04–08 → операции соответствующих строк | Order/Notification, MenuVersion/RecipeVersion, RobotRef, ExportBatch → C-01/05/07/10/I-03/09 → будущий день, версии, свежесть 30 с, повтор пакета без удвоения |

Там, где действие происходит на устройстве комплекса или во внешнем контуре, клиентский REST-эндпоинт не добавляется искусственно. Все 35 историй имеют экран либо автоматический результат в границах своего релиза. Этап 4 остается незавершенным.
