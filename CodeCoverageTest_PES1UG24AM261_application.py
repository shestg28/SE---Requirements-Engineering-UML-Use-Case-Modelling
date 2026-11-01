import pytest
from shopping_cart import item_total, cart_discount, shipping_fee


def test_item_total_food_and_gst():
    assert item_total("food", 100, 2) == 210


def test_item_total_each_known_category():
    assert item_total("electronics", 100, 1) == 118
    assert item_total("clothing", 100, 1) == 112


def test_item_total_bulk_discount():
    # Quantity >= 10 applies a 10% reduction before GST.
    assert item_total("food", 100, 10) == 945


def test_item_total_invalid_category():
    with pytest.raises(ValueError, match="unknown category"):
        item_total("books", 100, 1)


@pytest.mark.parametrize("price,qty", [(-1, 1), (100, 0), (100, -1)])
def test_item_total_invalid_price_or_quantity(price, qty):
    with pytest.raises(ValueError, match="invalid price or quantity"):
        item_total("food", price, qty)


def test_cart_discount_tiers_and_addons():
    assert cart_discount(5000, False, None) == 500
    assert cart_discount(2000, False, None) == 200
    assert cart_discount(1999, False, None) == 0
    assert cart_discount(1000, True, "FLAT10") == 200


def test_shipping_fee_cases():
    assert shipping_fee(1000, False, False) == 0
    assert shipping_fee(499, False, False) == 40
    assert shipping_fee(100, True, False) == 0
    assert shipping_fee(100, True, True) == 50
    assert shipping_fee(100, False, True) == 140
