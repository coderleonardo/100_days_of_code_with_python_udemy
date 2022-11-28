class Book2:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        # Declaring the privates attributes
        self.__price = price
        self.__discount = None


    # Method "set_discount"
    def set_discount(self, discount):
        self.__discount = discount

    # Method "get_price"
    def get_price(self):
        if self.__discount:
            return self.__price * (1- self.__discount)
        return self.__price

    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"

single_book = Book2('Two States', 1, 'Chetan Bhagat', 200)

bulk_books = Book2('Two States', 25, 'Chetan Bhagat', 200)
bulk_books.set_discount(0.20)

print(single_book.get_price())
print(bulk_books.get_price())
print(single_book)
print(bulk_books)