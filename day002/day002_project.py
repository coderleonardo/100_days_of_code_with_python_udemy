# Tip Calculator

print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip_pp = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

final_bill = total_bill * (1 + (tip_pp / 100))

people_bill = final_bill / num_people

print(f"Each person should pay: ${round(people_bill, 2)}")

