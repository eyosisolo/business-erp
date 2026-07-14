from models.product import Product
import pytest


def test_product_creation():
    product = Product("Lipstick", 450, 30)

    assert product.name == "Lipstick"
    assert product.price == 450
    assert product.stock == 30


def test_low_stock():
    product = Product("Perfume", 1200, 2)

    assert product.is_low_stock()


def test_invalid_price():

    with pytest.raises(ValueError):
        Product("Lipstick", -100, 30)


def test_empty_name():

    with pytest.raises(ValueError):
        Product("", 100, 5)


def test_negative_stock():

    with pytest.raises(ValueError):
        Product("Lipstick", 450, -5)