"""Number guessing game - practicing loops, conditionals and input."""
import random


def play():
    secret = random.randint(1, 100)
    attempts = 0
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = input("Your guess: ").strip()
