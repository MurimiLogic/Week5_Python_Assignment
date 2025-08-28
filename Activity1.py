#class chosen is Book
class Book:
    def __init__(self, title, author, isbn, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._price = price  # Encapsulation

    @property
    def price(self):
        return self._price
    
#property getter for further encapsulation
    @price.setter 
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Price: ${self.price:.2f}"

    def apply_discount(self, percentage):
        if percentage < 0 or percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100.")
        self.price = self.price * (1 - percentage / 100)

#inheritance from class Book with constructors
class EBook(Book):
    def __init__(self, title, author, isbn, price, file_size, format):
        super().__init__(title, author, isbn, price)
        self.file_size = file_size  # in MB
        self.format = format

# Polymorphism
    def display_info(self):  
        base_info = super().display_info()
        return f"{base_info}, Format: {self.format}, File Size: {self.file_size}MB"