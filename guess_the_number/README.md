# Guess the Number

A number guessing game built in Python to practice core programming concepts.

## Concepts Covered

- Variables (`number`, `guess`, `guess_count`)
- Loops (`while True`)
- User input with `input()`
- Output with `print()`
- Random number generation with `random.randint()`
- Conditional logic (`if/elif/else`)
- Input validation (`try/except`)
- Nested loops (play again loop inside difficulty selection)
- Difficulty levels and attempt limits
- “Hot or Cold” feedback system

## How It Works

1. The player chooses a difficulty:
   - Easy: 1–50, 10 attempts
   - Medium: 1–100, 7 attempts
   - Hard: 1–1000, 5 attempts
2. A random number is generated based on difficulty
3. The player has a limited number of guesses
4. After each guess, feedback is provided:
   - Too high / too low
   - “You're close!” if within 10
5. Player can play again after a round ends

## How to Run

In the terminal:
```bash
cd guess_the_number
python3 main.py