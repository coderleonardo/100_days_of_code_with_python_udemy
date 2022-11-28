class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price
        # Declaring the private attribute
        self.__discount = 0.10

    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}"

book1 = Book("Book 1", 12, "Author 1", 120)

# To access the attribute of a class instance (object) we use
# object_name.attrubute_name
print(book1.title)
print(book1.quantity)
print(book1.author)
print(book1.price)
print(book1.__discount) # return an error 


