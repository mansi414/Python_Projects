from art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

cpu_choice = random.randint(1, 101)


def play_game():

    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5
    user_guess = -1

    while attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess"))
        if user_guess == cpu_choice:
            return print(f"You got it! The answer was {cpu_choice}")
        elif user_guess > cpu_choice:
            print("Too High\nGuess again")
        else:
            print("Too low\nGuess again")
        attempts = attempts - 1

    return print("You've run out of guesses")


play_game()
