# Guess my number

# Learn about scopes for variables and functions.

def is_easy_or_hard(input):
    val = input.strip().lower()

    return val == 'easy' or val == 'hard'

from art import logo
from helpers import is_integer, ask_input
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.choice(range(1, 100))

difficulty = ask_input("Choose a difficulty. Type 'easy' or 'hard': ", is_easy_or_hard)
attempts = 10

if difficulty == 'hard':
    attempts = 5

guess = -1
while attempts > 0 and guess != number:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(ask_input("Make a guess: ", is_integer))

    if guess == number:
        print(f"You got it! The answer was {number}")
        continue
    elif guess > number:
        print("Too high.")
    else:
        print("Too low.")

    attempts -= 1

    if attempts > 0:
        print("Guess again")

if guess != number:
    print(f"You've run out of guesses, you lose. The number was {number}")
