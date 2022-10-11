from src.Condition import Condition


class Discount:
    condition: Condition
    price_discount: float
    available_in_weeks: list[int]

    def __init__(self, condition: Condition, price_discount: float, available_in_weeks: list[int]) -> None:
        self.condition = condition
        self.price_discount = price_discount
        self.available_in_weeks = available_in_weeks
