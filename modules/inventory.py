#Mini Project 1
import sqlite3
connection = sqlite3.connect("business.db")
cursor = connection.cursor()
def create_product_table():
   
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER NOT NULL
    )
    """)

def add_product(name, price, stock):
    cursor.execute("""
    INSERT INTO products(name, price, stock
    VALUES (?, ?, ?)
    """,(name, price, stock) )
    print("Product added!")
def view_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    print("\nProducts")
    for product in products:
     print(product)

def update_stock(name, stock):
    cursor.execute("UPDATE products SET stock = ? WHERE name = ?", (name, stock))
    print("Stock updated!")

def delete_product(name):
    cursor.execute("DELETE FROM products WHERE name = ?", ("name",))
    
connection.commit()
connection.close()