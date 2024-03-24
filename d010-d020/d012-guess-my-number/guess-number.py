# Guess my number

# Learn about scopes for variables and functions.

from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.choice(range(1, 100))

difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ")
attempts = 10
if difficulty == 'hard':
    attempts = 5

guess = -1
while attempts > 0 and guess != number:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

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
