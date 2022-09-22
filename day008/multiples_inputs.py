# functions with more than 1 input
def greet(name, location):
    print(f'Hello, {name}')

    print(f'What is it like in {location}')

greet('Leonardo', 'Brazil')

greet('Brazil', 'Leonardo') # positional argument

name, location = 'Leonardo', 'Brazil'
def greet_with_name(name=name, location=location): # keyword arguments
    print(f'Hello, {name}')

    print(f'What is it like in {location}')

greet_with_name(name=name, location=location)