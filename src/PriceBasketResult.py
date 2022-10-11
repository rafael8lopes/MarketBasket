class PriceBasketResult:
    sub_total: float
    offers: object
    total: float
    valid_items: list[str]

    def __init__(self, sub_total: float, offers: object, total: float, valid_items: list[str]) -> None:
        self.sub_total = sub_total
        self.offers = offers
        self.total = total
        self.valid_items = valid_items
