# control flow: if/else

"""
if condition:
    to this
else:
    to other thing
"""

# elif statement and nested if/else

"""
if ...:
    if ...:
        ...
    else ...:
        ...
else ...:
"""

""" 
if cond A:
    do A
elif cond B:
    do B
else:
    other thing
"""

height = int(input("Height? "))
bill = 0

if height > 120: # comparison operators: >, < >=, <=, ==, !=
    print("You can ride ride the rollercoaster!")
    age = int(input("Age? "))
    if age < 12:
        bill = 5
        print("$5")
    elif age <= 18:
        bill = 7
        print("$7")
    elif age >= 55 and age <= 65:
        print("$0")
    else:
        bill = 12
        print("$12")

    photo = input("Photo? Y or N ")
    if photo == "Y":
        bill += 3
    
    print(f"Your final bill is {bill}")

else:
    print("You can not ride the rollercoaster!")

# multiple if statements in sucession
"""
if A:
    do A
if B:
    do B
if C:
    do C
"""

# logical operators: and, or, not
"""
if A & B & C:
    do this
"""

"""
if A is true, B is true -> A and B is true
if A is true, B is false -> A or B is true
if A is false, B is false -> A or B is false
if A is true -> not A is false"""



