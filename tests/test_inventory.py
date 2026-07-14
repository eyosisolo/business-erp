from models.product import Product


def test_inventory_product():

    product = Product("Laptop", 50000, 8)

    assert product.name == "Laptop"
    assert product.price == 50000
    assert product.stock == 8

def test_product_string():

    product = Product("Lipstick", 450, 30)

    assert str(product) == "Lipstick | Price: 450 | Stock: 30"

def test_stock_equals_five():

    product = Product("Soap", 100, 5)

    assert product.is_low_stock()