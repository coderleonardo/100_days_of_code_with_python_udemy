# Calculator 
from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2): 
    return n1 / n2

operations_dict = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
}

def calculator():
    print(logo)
    print()
    
    again = True
    while again:

        num1 = float(input("First number? "))

        print("List of symbols:\n")
        for symbol in operations_dict:
            print(symbol)

        print()
        num2 = float(input("Second number? "))


        print()
        oper_symbol = input("Choose an operation: ")
        print()

        answer = operations_dict[oper_symbol](num1, num2)
        print(f"Result: {num1} {oper_symbol} {num2} = {answer}")

        print()
        another = input("Do you want to do another operation? ('yes' or 'no') ")
        if another != 'yes': 
            again = False


calculator()