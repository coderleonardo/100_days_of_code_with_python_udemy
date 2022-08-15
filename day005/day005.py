# using for loop

# for item in list_of_items:
    # do that

count = 1
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(count)
    count += 1

# using for loop with "range"

# for number in range(a, b): b is not incluse
    # do something

for number in range(1, 10):
    if number % 2 == 0:
        print(number)

for number in range(1, 10, 3):
    print(number)

total = 0
for num in range(1, 101):
    total += num
print(total)
