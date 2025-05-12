# Rock, Paper, Scissors – Best of 5

A Python implementation of the classic game, refactored with clean functions, input validation, and a best-of-five match system.

## Concepts Covered

- Lists (`["rock", "paper", "scissors"]`)
- User input with `input()` and normalization with `.lower()`
- Random choice generation with `random.choice()`
- Conditional logic (`if/elif/else`) for game rules
- Functions for modular, readable code:
  - `get_player_choice()`
  - `get_computer_choice()`
  - `determine_winner()`
  - `play_round()`
  - `main()`
- Return values to communicate game state
- Looping for repeated rounds and matches
- Input validation with looped error handling
- Game state tracking with `player_wins`, `computer_wins`

## How It Works

1. The game plays multiple rounds of Rock, Paper, Scissors
2. The first to 3 wins is declared the match winner (Best of 5 format)
3. Player input is validated (must be "rock", "paper", or "scissors")
4. After each round:
   - The winner is announced
   - The score is displayed
5. Game ends when either the player or the computer reaches 3 wins

## How to Run

In the terminal:
```bash
cd rock_paper_scissors
python3 main.py