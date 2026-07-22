import sqlite3

class ProductRepository:
    def __init__(self):
        self.connection = sqlite3.connect("business.db")
        self.cursor = self.connection.cursor()
    
    def save(self, product):
        self.cursor.execute(
            """
            INSERT INTO products (name, price, stock)
            VALUES (?,?,?)
            """,
            (
             product.name,
             product.price,
             product.stock
            )
        )

# find_by_name()
    def find_by_name(self, name):

        self.cursor.execute("SELECT * FROM products WHERE name = ?", (name,)
        )

        return self.cursor.fetchone()

#exists()
    def exists(self, name):
        return self.find_by_name(name) is not None

    def search(self, keyword):
        self.cursor.execute("""SELECT * FROM products WHERE name LIKE ?""", (f"%{keyword}%",))
        return self.cursor.fetchall()

def low_stock_products(self):
    self.cursor.execute("""SELECT * FROM products WHERE stock <= 5""")

    return self.cursor.fetchall()

def inventory_value(self):
    self.cursor.execute("""SELECT SUM(price * stock) FROM products""")

    return self.cursor.fetchone()[0]

value = ProductRepository().inventory_value()

print(f"Total Inventory Value: {value}")