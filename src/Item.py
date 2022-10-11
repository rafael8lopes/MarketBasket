from src.Discount import Discount


class Item:
    name: str
    current_price: float
    discounts: list[Discount]

    def __init__(self, name: str, current_price: float, discounts: list[Discount]) -> None:
        self.name = name
        self.current_price = current_price
        self.discounts = discounts
