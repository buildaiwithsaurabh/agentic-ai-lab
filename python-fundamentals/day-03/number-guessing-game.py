# NUMBER GUESSING GAME

import random

# Generate random number between 1 and 100
number = random.randint(1, 100)

guesses = 0
running = True

print("Python Number Guessing Game")
print("Guess a number between 1 and 100")


while running:

    guess = input("Enter your guess: ")

    # Validate input
    if guess.isdigit():

        guess = int(guess)
        guesses += 1

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100")

        elif guess < number:
            print("Too Low! Try Again")

        elif guess > number:
            print("Too High! Try Again")

        else:
            print(f"Correct! The number was {number}")
            print(f"Total Guesses: {guesses}")
            running = False

    else:
        print("Invalid Input! Enter numbers only")