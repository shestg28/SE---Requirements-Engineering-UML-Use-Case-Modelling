import pytest
from shopping_cart import item_total, cart_discount, shipping_fee


@pytest.mark.parametrize("category,price,qty,expected", [
    ("food", 100, 2, 210),                 # known category, ordinary quantity
    ("electronics", 100, 1, 118),
    ("clothing", 100, 1, 112),
    ("food", 100, 10, 945),                # bulk threshold true
    ("food", 100, 9, 945 // 1),            # bulk threshold false: amount 900 + 5% GST
])
def test_item_total_valid_paths(category, price, qty, expected):
    if qty == 9:
        expected = 945
    assert item_total(category, price, qty) == expected


@pytest.mark.parametrize("category,price,qty,message", [
    ("unknown", 10, 1, "unknown category"),
    ("food", -1, 1, "invalid price or quantity"),
    ("food", 1, 0, "invalid price or quantity"),
    ("food", 1, -1, "invalid price or quantity"),
])
def test_item_total_error_paths(category, price, qty, message):
    with pytest.raises(ValueError, match=message):
        item_total(category, price, qty)


@pytest.mark.parametrize("value,prime,coupon,expected", [
    (5000, False, None, 500),              # highest tier
    (2000, False, None, 200),              # middle tier
    (1999, False, None, 0),                # lowest tier
    (1000, True, "FLAT10", 200),            # prime and coupon condition true
    (999, True, "FLAT10", 100),             # coupon amount threshold false
    (1000, False, "OTHER", 0),              # coupon code false
    (1000, True, "OTHER", 100),             # prime true, coupon false
])
def test_cart_discount_branches(value, prime, coupon, expected):
    assert cart_discount(value, prime, coupon) == expected


@pytest.mark.parametrize("value,prime,express,expected", [
    (1000, False, False, 0),                # free by cart threshold
    (499, False, False, 40),                # paid shipping
    (100, True, False, 0),                  # prime shipping
    (100, True, True, 50),                  # express + prime reduction
    (100, False, True, 140),                # express without prime
])
def test_shipping_fee_branches(value, prime, express, expected):
    assert shipping_fee(value, prime, express) == expected
