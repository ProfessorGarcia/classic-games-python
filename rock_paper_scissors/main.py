import random

def get_player_choice():
    options = ["rock", "paper", "scissors"]
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in options:
            return choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def determine_winner(player, computer):
    print(f"You picked: {player}")
    print(f"Computer picked: {computer}")

    if player == computer:
        print("It's a tie!")
        return "tie"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ): 
        print("You win!")
        return "player"
    else:
        print("You lose!")
        return "computer"

def play_round():
    player = get_player_choice()
    computer = get_computer_choice()
    return determine_winner(player, computer)

def main():
    print("Welcome to Rock, Paper, Scissors - Best of 5!")

    player_wins = 0
    computer_wins = 0

    while player_wins < 3 and computer_wins < 3:
        result = play_round() # Will return "player", "computer", or "tie"

        if result == "player":
            player_wins += 1
        elif result == "computer":
            computer_wins += 1

        print(f"Score - You: {player_wins} | Computer: {computer_wins}\n")

    # Declare winner
    if player_wins == 3:
        print("You won the match!")
    else:
        print("You lost the match.")

    print("Thanks for playing!")

# Run the game
main()