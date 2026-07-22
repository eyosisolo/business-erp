
from modules import inventory
from models.product import Product
from repositories.product_repository import ProductRepository
from utils.logger import logger

class InventoryService:
    def add_new_product(self, name, price, stock):
        product = Product(name, price, stock)
        
        repository = ProductRepository()
        repository.save(product)

        logger.info(f"Product added: {name}")

        print("Product added successfully!")

repository = ProductRepository()

if repository.exists(name):

    logger.warning(f"Duplicate product: {name}")

    print("Product already exists.")

    return