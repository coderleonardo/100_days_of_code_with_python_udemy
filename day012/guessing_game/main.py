# Number Guessing Game Objectives:

# Include an ASCII art logo.
from art import logo
print(logo)

# Allow the player to submit a guess for a number between 1 and 100.
print("Welcome to the Number Guessing Game!")
import random
the_number = random.choice(list(range(1, 101)))

print("I'm thinking of a number between 1 and 100.")
difficuty = input("Choose a difficuty. Type 'easy' or 'hard': ")

n_chances = None
if difficuty == 'easy':
    n_chances = 10
else:
    n_chances = 5

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
while n_chances >= 0:
    print(f"You have {n_chances} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    
    if guess == the_number:
        print("You got the right answer.")
        n_chances = -1
    elif guess > the_number:
        print("Too high.\nGuess again.")
    elif guess < the_number:
        print("Too low.\nGuess again.")

        
    n_chances -= 1
    

