import random

play_again = 'y'

while play_again == 'y':
    options = ["rock", "paper", "scissors"]

    player_choice = input("Choose rock, paper, or scissors: ").lower()
    print("You picked:", player_choice)

    computer_choice = random.choice(options)
    print("Computer picked:", computer_choice)

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win")
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Play again? (y/n): ").lower()