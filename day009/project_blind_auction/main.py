from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)
print()

bids_dict = {}

name = input("Name, please: ")
bid_price = float(input("Bid price: $"))
print()

bids_dict[name] = bid_price

more_bids_dict = {"yes": True, "no": False}
more_bids = input("There are other users who want to bid? answer with 'yes' or 'no': ")
print()

if more_bids_dict[more_bids] == True:
    clear()
    while more_bids_dict[more_bids]:
        name = input("Name, please: ")
        bid_price = float(input("Bid price: $"))
        print()

        bids_dict[name] = bid_price

        more_bids = input("There are other users who want to bid? answer with 'yes' or 'no': ")
        print()

best_buyer = max(bids_dict, key=bids_dict.get)

print(f"The best buyer is {best_buyer}, with the bid price {bids_dict[best_buyer]}.")
