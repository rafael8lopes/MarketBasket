from PriceBasket import price_basket
from src.Offer import Offer


def test_price_basket_without_discounts():
    result = price_basket(["Soup", "Milk"])
    assert result.sub_total == 1.95
    assert result.offers == {}
    assert result.total == 1.95
    assert result.valid_items == ["Soup", "Milk"]


def test_price_basket_with_discounts():
    result = price_basket(["Soup", "Soup", "Soup", "Bread"])
    assert result.sub_total == 2.75
    assert result.offers['Bread'].__str__() == Offer("Bread", 50, 0.4).__str__()
    assert result.total == 2.35
    assert result.valid_items == ["Soup", "Soup", "Soup", "Bread"]
