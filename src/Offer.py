class Offer:
    item_name: str
    discount: float
    price_reduction: float

    def __init__(self, item_name: str, discount: float, price_reduction: float) -> None:
        self.item_name = item_name
        self.discount = discount
        self.price_reduction = price_reduction

    def __str__(self):
        return {
            "item_name": self.item_name,
            "discount": self.discount,
            "price_reduction": self.price_reduction
        }
