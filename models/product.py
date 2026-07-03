class Product:
    def __init__(self, name, price, stock):
        if name.strip() == "":
            raise ValueError("Name cannot be empty.")

        if price <= 0:
            raise ValueError("Price must be greater than zero.")

        if stock < 0:
            raise ValueError("Stock cannot be negative.")

        self.name = name
        self.price = price
        self.stock = stock

    def display(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Stock:", self.stock)