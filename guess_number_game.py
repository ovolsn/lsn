import random

def guess_number_game():
    """A simple number guessing game with difficulty levels."""
    print("Welcome to the Guess the Number Game!")
    print("Choose a difficulty level:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")
    print("4. Expert (1-500)")

    # Get user input for difficulty level
    while True:
        try:
            difficulty = int(input("Enter the difficulty level (1/2/3/4): "))
            if difficulty not in (1, 2, 3, 4):
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Set the range based on difficulty level
    if difficulty == 1:
        lower, upper = 1, 50
    elif difficulty == 2:
        lower, upper = 1, 100
    elif difficulty == 3:
        lower, upper = 1, 200
    else:
        lower, upper = 1, 500

    print(f"I'm thinking of a number between {lower} and {upper}.")

    # Generate a random number within the chosen range
    target_number = random.randint(lower, upper)
    attempts = 0

    while True:
        # Get user input
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        # Increment the number of attempts
        attempts += 1

        # Check the guess
        if guess < lower or guess > upper:
            print(f"Your guess is out of range. Please guess a number between {lower} and {upper}.")
        elif guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_number_game()
