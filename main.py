#Mini Project 2
from modules import inventory
from models.product import Product
from services.inventory_service import InventoryService
from repositories.product_repository import ProductRepository

service = InventoryService()
print("Business ERP Database Started")
#Mini Project 3 – Build a Simple Menu
def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Create Product Table")
        print("2. Add Product")
        print("3. View Products")
        print("4. Update Stock")
        print("5. Delete Product")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            inventory.create_product_table()
            print("Product table created!")
        elif choice == "2":

            while True:
                name = str(input("Enter product name:")).strip()
                if name != "":
                     break
                print("Product name cannot be empty. Please enter a valid name.")
                
            
            while True:
              price = float(input("Price: "))
              if price > 0:
               break
              print("Price must be greater than zero.")
            
            while True:
              stock = int(input("Stock: "))
              if stock >= 0:
               break
            print("Stock cannot be negative.")
           
            service.add_new_product(name, price, stock)
        elif choice == "3":
            inventory.view_products()
    
        elif choice == "4":

            keyword = input("Search: ")
 
            products = ProductRepository().search(keyword)

            for product in products:

                print(product)
        
        elif choice == "5":
            name = input("Enter product name to delete: ")
            inventory.delete_product(name)
            print(f"Product '{name}' deleted!")
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
         print("Invalid choice. Please try again.")
         
         
if __name__ == "__main__":
    main_menu()

products = ProductRepository().low_stock_products()

for product in products:

    print(product)

