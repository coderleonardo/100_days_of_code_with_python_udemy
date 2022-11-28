class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price

# The "__init__" special method, also known as a "Constructor", is used to 
# initialize the Book class with attributes such as title, quantity, author, 
# and price

# Note that the term "self" in the attributes refers to the corresponding
# instances

# Differents instances of the Book class
book1 = Book("Book 1", "The book 1", "Author 1", 120)
book2 = Book("Book 2", "The book 2", "Author 2", 220)
book3 = Book("Book 3", "The book 3", "Author 3", 320)

print(book1) # return the class and memory location
print(book2) # return the class and memory location
print(book3) # return the class and memory location

print()

# Book class with the special method "__repr__"
class Book2:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price

    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}"

# The "__repr__" provides specific information on the qualities

book1 = Book2("Book 1", "The book 1", "Author 1", 120)
book2 = Book2("Book 2", "The book 2", "Author 2", 220)
book3 = Book2("Book 3", "The book 3", "Author 3", 320)

print(book1) 
print(book2) 
print(book3)