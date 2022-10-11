from __future__ import annotations
from resources.items import items
from src.Item import Item
from src.DiscountPrice import DiscountPrice
from src.Offer import Offer
from src.PriceBasketResult import PriceBasketResult
import sys
import logging
from datetime import date

log = logging.getLogger(__name__)


# gets a system item from by 'item_name'
def get_item(item_name: str) -> Item:
    for item in items:
        if item_name == item.name:
            return item


# gets item price with discount if available and the discount percentage
def get_item_discount(item: Item, valid_items: list[str]) -> DiscountPrice:
    current_week = date.today().isocalendar()[1]

    if len(item.discounts) == 0:
        return DiscountPrice(item.current_price, 0)
    else:
        for discount in item.discounts:
            # assuming that empty 'available_in_weeks' field is an all weeks discount
            # applies discount if empty or current week in weeks list and discount condition is valid
            if (current_week in discount.available_in_weeks or len(discount.available_in_weeks) == 0) and \
                    valid_items.count(discount.condition.item) >= discount.condition.min_amount:
                return DiscountPrice((item.current_price * (100 - discount.price_discount)) / 100, discount.price_discount)

    return DiscountPrice(item.current_price, 0)


def price_basket(argv_items) -> PriceBasketResult:
    valid_items = []
    sub_total = 0
    total = 0
    offers = {}

    # filter valid items from arguments
    for argv_item in argv_items:
        if argv_item not in [item.name for item in items]:
            log.warning("Item '%s' doesn't exist on system items list", argv_item)
            continue
        else:
            valid_items.append(argv_item)

    for item_name in valid_items:
        item = get_item(item_name)

        sub_total += item.current_price
        discount_price = get_item_discount(item, valid_items)
        total += discount_price.real_price

        # if item has a discount, saves this information for later displays to user
        if item.current_price != discount_price.real_price:
            offers[item.name] = Offer(item.name, discount_price.discount,
                                      item.current_price - discount_price.real_price +
                                      (offers[item.name].price_reduction if item.name in offers else 0))

    return PriceBasketResult(round(sub_total, 2), offers, round(total, 2), valid_items)


def main() -> None:
    # removes the 'PriceBasket' argument
    del sys.argv[0]
    result = price_basket(sys.argv)

    # prints the basket information
    print("Subtotal", round(result.sub_total, 2))

    if len(result.offers) == 0:
        print("(no offers available)")
    else:
        for offer_name in result.offers:
            print("{} {}% off: -€{}".format(result.offers[offer_name].item_name, result.offers[offer_name].discount,
                                            round(result.offers[offer_name].price_reduction, 2)))

    print("Total", round(result.total, 2))

    for valid_item in result.valid_items:
        print(valid_item)


main()
