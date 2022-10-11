class Condition:
    item: str
    min_amount: int

    def __init__(self, name: str, min_amount: int) -> None:
        self.item = name
        self.min_amount = min_amount
