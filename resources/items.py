from src.Item import Item
from src.Discount import Discount
from src.Condition import Condition

items: list[Item] = [
    Item("Soup", 0.65, []),
    Item("Bread", 0.80, [Discount(Condition("Soup", 2), 50, [])]),
    Item("Milk", 1.30, []),
    Item("Apples", 1.00,  [Discount(Condition("Apples", 1), 10, [48])])
]
