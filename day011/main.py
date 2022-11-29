############### Blackjack Project #####################

from art import logo
from Hands import HandsInitializer
# Lib to choose a random element from the cards list
import random

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
print()

if play == "y":
    print(logo)
    print()

    #        A                           Q   K   J 
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    player = HandsInitializer("Leonardo")
    computer = HandsInitializer("Computer")

    # Initial cards
    for i in range(2):
        player.cards.append(random.choice(cards))
        computer.cards.append(random.choice(cards))

    player.update_score()
    computer.update_score()

    print(player)
    computer.first_card_infos()
    print()

    continue_ = True

    if player.score == 21:
        print(f"{player.name} wins!!!")
        print()
        continue_ = False
    elif computer.score == 21:
        print(f"{computer.name} wins!!!")
        print()
        continue_ = False

    while continue_:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        if another_card == "y":
            player.cards.append(random.choice(cards))
            player.update_score()

            computer.cards.append(random.choice(cards))
            computer.update_score()

            print(player)
            computer.first_card_infos()
            print()

            if player.score >= 21:
                print(f"{computer.name} wins!!!")
                print()
                continue_ = False
            elif computer.score >= 21:
                print(f"{player.name} wins!!!")
                print()
                continue_ = False
            elif player.score == computer.score:
                print("It's a Draw!!!")
                print()
                continue_ = False
        else:
            continue_ = False

    print("End of game.")
    print()

    print(f"{player.name}'s final hand: {player.cards}. Final score: {player.score}")
    print(f"{computer.name}'s final hand: {computer.cards}. Final score: {computer.score}")

else:
    print("Exited.")