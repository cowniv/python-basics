"""Number guessing game - practicing loops, conditionals and input."""
import random


def play():
    secret = random.randint(1, 100)
    attempts = 0
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = input("Your guess: ").strip()
        if not guess.isdigit():
            print("Please enter a whole number.")
            continue

        attempts += 1
        guess = int(guess)

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"You got it in {attempts} tries!")
            break
