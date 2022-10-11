class DiscountPrice:
    real_price: float
    discount: float

    def __init__(self, real_price: float, discount: float) -> None:
        self.real_price = real_price
        self.discount = discount
