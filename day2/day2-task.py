from dataclasses import dataclass
from typing import Literal


@dataclass
class Item:
    price: float
    qty: int
    discount: float = 0
    discount_type: Literal["percent", "flat", None] = None


@dataclass
class Customer:
    name: str
    type: Literal["regular", "premium"] = "regular"


@dataclass
class Order:
    items: list[Item]
    country: str
    customer: Customer
    coupon: str | None = None


TAX_RATES: dict[str, float] = {"IN": 0.18, "US": 0.07}
DEFAULT_TAX_RATE = 0.10

COUPON_DISCOUNTS: dict[str, float] = {"SAVE10": 0.10, "SAVE20": 0.20}

PREMIUM_DISCOUNT_THRESHOLD = 1000
PREMIUM_DISCOUNT_AMOUNT = 50
FREE_SHIPPING_THRESHOLD = 500
SHIPPING_COST = 40


def apply_item_discount(item: Item) -> float:
    """Return the per-unit price of an item after its own discount, floored at 0."""
    if not item.discount:
        return item.price
    if item.discount_type == "percent":
        discounted = item.price - (item.price * item.discount / 100)
    else:  # "flat"
        discounted = item.price - item.discount
    return max(discounted, 0)


def calculate_items_subtotal(items: list[Item]) -> float:
    """Sum (discounted unit price * quantity) across all items."""
    return sum(apply_item_discount(item) * item.qty for item in items)


def apply_coupon(subtotal: float, coupon: str | None) -> float:
    """Apply a percentage-off coupon code, if valid, to the subtotal."""
    discount = COUPON_DISCOUNTS.get(coupon, 0) if coupon else 0
    return subtotal * (1 - discount)


def calculate_tax(amount: float, country: str) -> float:
    """Return tax owed for a given country's rate (falls back to a default rate)."""
    rate = TAX_RATES.get(country, DEFAULT_TAX_RATE)
    return amount * rate


def apply_premium_discount(total: float, customer: Customer) -> float:
    """Give premium customers a flat discount once their order passes a threshold."""
    if customer.type == "premium" and total > PREMIUM_DISCOUNT_THRESHOLD:
        return total - PREMIUM_DISCOUNT_AMOUNT
    return total


def calculate_shipping(total: float) -> float:
    """Flat shipping fee below a free-shipping threshold, otherwise free."""
    return 0 if total >= FREE_SHIPPING_THRESHOLD else SHIPPING_COST


def process_order(order: Order) -> float:
    """Compute the final payable total for an order, applying discounts, tax, and shipping."""
    subtotal = calculate_items_subtotal(order.items)
    subtotal = apply_coupon(subtotal, order.coupon)

    total = subtotal + calculate_tax(subtotal, order.country)
    total = apply_premium_discount(total, order.customer)
    total += calculate_shipping(total)

    return round(total, 2)

if __name__ == "__main__":

    sample_order = Order(
        items=[
            Item(price=500, qty=2, discount=10, discount_type="percent"),
            Item(price=300, qty=1, discount=50, discount_type="flat"),
            Item(price=150, qty=3),
        ],
        country="IN",
        customer=Customer(name="Arivazhagan", type="premium"),
        coupon="SAVE10",
    )

    final_total = process_order(sample_order)
    print("Returned value:", final_total)