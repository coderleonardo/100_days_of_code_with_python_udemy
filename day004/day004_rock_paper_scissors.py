rock = '''\n
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)\n'''

scissor = '''\n
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)\n'''

paper = '''\n
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)\n'''

import random
index_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

game_choices = [rock, paper, scissor]
choice = game_choices[index_choice]

rand_index_choice = random.randint(0, 2)
random_choice = game_choices[rand_index_choice]

print(f"Player choice:\n{choice}")
print(f"Computer choice:\n{random_choice}")

if (index_choice == rand_index_choice):
    print("It's a draw")
elif (index_choice == 0) and (rand_index_choice == 2):
    print("You win!")
elif (index_choice == 1) and (rand_index_choice == 0):
    print("It's a draw")
elif (index_choice == 2) and (rand_index_choice == 1):
    print("It's a draw")
else:
    print("You lose!")


