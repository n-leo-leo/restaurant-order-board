# Диаграмма классов

Модель охватывает MVP и первый релиз. Склад, роботы, эквайринг и касса остаются внешними системами. Приложение хранит необходимые ссылки и результаты их операций. Диаграммы разделены по областям; одинаковое имя обозначает одну сущность. Атрибуты и ограничения раскрыты в [словаре](entities.md), переходы — в [модели состояний](order-states.md).

## Каталог

```mermaid
classDiagram
direction TB
class MenuVersion
class Category
class MenuEntry
class Dish
class RecipeVersion
class RecipeLine {
  decimal quantity
  string unit
}
class IngredientRef
class PromotionRule
class ComboLine {
  int quantity
}
MenuVersion "1" *-- "0..*" MenuEntry
Category "1" --> "0..*" MenuEntry
MenuEntry "0..*" --> "1" Dish
MenuEntry "0..*" --> "0..1" RecipeVersion
RecipeVersion "1" *-- "1..*" RecipeLine
RecipeLine "0..*" --> "1" IngredientRef
MenuVersion "1" --> "0..*" PromotionRule
MenuEntry "1" *-- "0..*" ComboLine : combo
ComboLine "0..*" --> "1" MenuEntry : component
```

[Открыть схему в полном размере](../assets/stage2-class-diagram-1.svg).

## Ресторан и покупка

```mermaid
classDiagram
direction TB
class Restaurant {
  UUID restaurantId
  string timezone
  bool salesStopped
}
class TradingDay
class Device
class MenuVersion
class Session
class Cart
class CartLine
class MenuEntry
class Order {
  UUID purchaseId
  string publicNumber
  bigint totalKopecks
  string state
}
class OrderLine
Restaurant "1" --> "0..*" TradingDay
Restaurant "1" --> "1..*" Device
TradingDay "0..*" --> "1" MenuVersion : uses
Device "1" --> "0..*" Session : kiosk
Session "1" *-- "1" Cart
Cart "1" *-- "0..*" CartLine
CartLine "0..*" --> "1" MenuEntry
Cart "0..1" --> "0..*" Order : saved purchases
TradingDay "1" --> "0..*" Order
Order "1" *-- "1..*" OrderLine
OrderLine "0..*" --> "1" MenuEntry : source
```

[Открыть схему в полном размере](../assets/stage2-class-diagram-2.svg).

`Device` различает киоск, табло и терминал сотрудника. Ячейка имеет отдельный жизненный цикл. Заказ не наследуется от корзины. После сохранения снимка изменение состава создает новую покупку; это разрешено только после безопасного завершения предыдущей оплаты. Повтор оплаты неизмененной покупки после отказа использует тот же purchaseId и новую попытку.

Комбо состоит из готовых блюд, ссылки на себя и циклы запрещены. У обычной позиции нет ComboLine. В MVP меню и правила загружаются до запуска; редакторы US-27–30 относятся к первому релизу. Одна версия меню может использоваться несколькими торговыми днями.

## Оплата и документы

```mermaid
classDiagram
direction TB
class Order
class Reservation
class PaymentAttempt
class Refund
class FiscalOperation
class PrintTask
class Ticket
Order "1" --> "0..*" Reservation
Order "1" --> "0..*" PaymentAttempt
PaymentAttempt "0..1" --> "1" Reservation : uses
Order "1" --> "0..1" Refund
Refund "0..1" --> "1" PaymentAttempt : successful
Order "1" --> "0..*" FiscalOperation
FiscalOperation "0..*" --> "0..1" Refund
Order "1" --> "0..*" PrintTask
PrintTask "0..*" --> "0..1" FiscalOperation
PrintTask "0..*" --> "0..1" Ticket
```

[Открыть схему в полном размере](../assets/stage2-class-diagram-3.svg).

## Кухня и ячейка

```mermaid
classDiagram
direction TB
class Order
class KitchenJob
class RobotRef
class CellRef
class CellAssignment
class Ticket
Order "1" --> "0..1" KitchenJob
KitchenJob "0..*" --> "0..1" RobotRef
Order "1" --> "0..*" CellAssignment
CellRef "1" --> "0..*" CellAssignment
Order "1" --> "0..1" Ticket
```

[Открыть схему в полном размере](../assets/stage2-class-diagram-4.svg).

## Помощь и служебные данные

```mermaid
classDiagram
direction TB
class Order
class CellRef
class Problem
class Notification
class Employee
class Role
class AuditEvent
class DeliveryTask
Order "0..1" --> "0..*" Problem
CellRef "0..1" --> "0..*" Problem
Problem "1" --> "1..*" Notification
Employee "0..1" --> "0..*" Problem : accepts
Employee "0..*" --> "1..*" Role
Order "0..1" --> "0..*" AuditEvent
Order "0..1" --> "0..*" DeliveryTask
```

[Открыть схему в полном размере](../assets/stage2-class-diagram-5.svg).

RobotRef и CellRef — ссылки на оборудование внешнего комплекса. История назначений ячейки сохраняется, одновременно активно только одно. Резерв создается до попытки и может остаться без нее. Каждая попытка использует один отдельный резерв; после отказа он освобождается, перед новой попыткой создается новый. Успешное списание по покупке не более одного. Возврат полный, повторные обращения относятся к одной операции.

## Первый релиз

```mermaid
classDiagram
direction LR
class Order
class LoyaltyProfileRef
class BonusOperationRef
class GiftAllocation
class ExportBatch
class ExportLine
class TradingDay
LoyaltyProfileRef "0..1" --> "0..*" Order
Order "1" --> "0..*" BonusOperationRef
Order "1" --> "0..1" GiftAllocation
TradingDay "1" --> "0..*" ExportBatch
ExportBatch "1" *-- "1..*" ExportLine
ExportLine "0..*" --> "1" Order
```

[Открыть схему в полном размере](../assets/stage2-class-diagram-6.svg).

Баланс принадлежит внешней системе лояльности. Наличная оплата использует PaymentAttempt, возврат — Refund. Правила бонусов определяются A-10. Конструктор комбобургера исключен.

Основание: БТ-01–18, US-01–35, A-01–16.
