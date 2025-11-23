import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (1–10): "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a number.")

number_guessing_game()
