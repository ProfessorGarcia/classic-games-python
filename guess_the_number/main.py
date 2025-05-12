import random

print("Welcome to the Guess the Number game!")
number = random.randint(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        break
# This is a simple number guessing game where the user has to guess a randomly generated number between 1 and 100.
