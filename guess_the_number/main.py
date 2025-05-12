import random

play_again = 'y' # GAME LOOP: This controls whether the user wants to play again.

while play_again == 'y':
    print("\n Welcome to Guess the Number!")
    
    difficulty = input("Choose difficulty - Easy (E), Medium (M), Hard (H): ").lower() # Select difficulty

    if difficulty == "e":
        number = random.randint(1, 50)
        max_attempts = 10
    elif difficulty == "m":
        number = random.randint(1, 100)
        max_attempts = 7
    elif difficulty == "h": 
        number = random.randint(1, 1000)
        max_attempts = 5
    else:
        print("Invalid choice. Defaulting to Medium.")
        number = random.randint(1, 100)
        max_attempts = 7

    guess_count = 0 # Track how many guesses it takes

    while True: # ROUND LOOP: This runs until the correct number is guessed
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("That wasn't a valid number. Try again.")
            continue

        guess_count += 1

        difference = abs(number - guess) # Hot or Cold Feedback
        if difference <= 10:
            print("You're very close!")
        else:
            print("You're way off.")

        if guess < number: # Guess evaluation
            print("Too low!")
        elif guess > number: 
            print("Too high!")
        else: 
            print(f"Correct! It took you {guess_count} guesses.")
            break # Exit the round loop
    
        if guess_count >= max_attempts:
            print(f"Out of guesses. the number was {number}.")
            break

    play_again = input("Play again? (y/n): ").lower()  # Ask to play again

print("Thanks for playing!")