# Guess my number

# Learn about scopes for variables and functions.

HINTS = True

def is_valid_choice(input):
    val = input.strip().lower()

    return val == 'easy' or val == 'hard' or val == 'x-hard'

def cheat(min_number, max_number, guess):
    to_lower = guess - min_number
    to_higher = max_number - guess
    new_guess = guess

    if to_lower > to_higher:
        new_guess = guess - int(to_lower / 2)
    elif to_higher > to_lower:
        new_guess = guess + int(to_higher / 2)
    elif to_higher > 1:
        new_guess = guess + 1

    return new_guess

from art import logo
from helpers import is_integer, ask_input
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)

if HINTS:
    print(f"Psst, the number is {number}")

difficulty = ask_input("Choose a difficulty. Type 'easy', 'hard' or 'x-hard': ", is_valid_choice)
attempts = 10

if difficulty == 'hard' or difficulty == 'x-hard':
    attempts = 5

guess = -1
min = 0
max = 101
while attempts > 0 and guess != number:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(ask_input("Make a guess: ", is_integer))

    if difficulty == 'x-hard' and guess == number:
        number = cheat(min, max, guess)

        if HINTS:
            print(f"Psst, now the number is {number}")

    if guess == number:
        print(f"You got it! The answer was {number}")
        continue
    elif guess > number:
        max = guess
        print("Too high.")
    else:
        min = guess
        print("Too low.")

    attempts -= 1

    if attempts > 0:
        print("Guess again")

if guess != number:
    print(f"You've run out of guesses, you lose. The number was {number}")
