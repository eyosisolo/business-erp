from modules import inventory
from models.product import Product

class InventoryService:
    def add_new_product(self, name, price, stock):
        product = Product(name, price, stock)
        inventory.add_product(
            product.name,
            product.price,
            product.stock
            )
        print("Product added successfully!")