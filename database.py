#SQL
#cursor.execute(...) sends an SQL command to the database.
#VALUES (?, ?, ?) This is safer and protects against SQL injection, a common security vulnerability. It's the professional way to pass values into SQL queries.

#Mini Project 1 — Create Your First Database
import sqlite3
connection = sqlite3.connect("business.db")
cursor = connection.cursor()
print("Connected to Business ERP Database!")

#Mini Project 2 — Create Your First Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL
)
""")

print("Products table created successfully!")

#Mini Project 3 Insert Your First Product

cursor.execute("""
INSERT INTO products(name, price, stock)
VALUES (?, ?, ?)
""", ("Lipstick", 450, 30))


print("Product added!")
# Mini Project 4 — View All Products
cursor.execute("SELECT * FROM products")
products = cursor.fetchall()
print("\nProducts")
for product in products:
    print(product)

# Mini Project 5 — Search for One Product
#("Lipstick",) That's a tuple with one item. Without the comma, Python doesn't treat it as a tuple.
cursor.execute("SELECT * FROM products WHERE name = ?", ("Lipstick",))
product = cursor.fetchone()
print(product)

#Mini Project 6 — Update Stock
cursor.execute("UPDATE products SET stock = ? WHERE name = ?", (25, "Lipstick"))
print("Stock updated!")

#Mini Project 7 — Delete a Product
cursor.execute("DELETE FROM products WHERE name = ?", ("Lipstick",))
print("Product deleted!")

connection.commit()
connection.close()