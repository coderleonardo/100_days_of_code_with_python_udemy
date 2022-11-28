class OverloadingDemo:
    def add(self, x, y):
        print(x + y)

    def add(self, x, y, z):
        print(x + y + z)

# Python doesn't support Method Overloading by default.
# Python only remembers the most recent definition of a function.

obj = OverloadingDemo()
obj.add(2, 3) # return an error