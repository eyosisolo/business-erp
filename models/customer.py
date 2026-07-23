class Customer:
    def __init__(self, name, phone, email):

        if name.strip() == "":
            raise ValueError("Name cannot be empty.")

        if phone.strip() == "":
            raise ValueError("Phone number cannot be empty.")
        self.name = name 
        self.phone = phone
        self.email = email

    def display(self):
        print("Name:", self.name)
        print("Phone:", self.phone)     
        print("Email:", self.email)

    def __str__(self):
        return (
            f"{self.name} |" 
            f"{self.phone} | " 
            f"{self.email}"
        )