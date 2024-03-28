# Higher of Lower

# Create a game from scratch, trying to see if the user can guess
# correctly which celebrity has more or less followers than other.

# Nothing new to learn on this day, but a practice to do something
# on our own.

def valid_input(input):
    input = input.strip()

    return input == 'A' or input == 'B'

def format_data(data):
    return f"{data['name']}, {data['description']}, from {data['country']}"

def correct_guess(guess, option_a, option_b):
    if option_a > option_b:
        return guess == 'A'
    else:
        return guess == 'B'

def get_new_slots(option_a, option_b):
    option_a = option_b

    while option_a == option_b:
        option_b = random.choice(data)

    return option_a, option_b

from art import logo, vs
from data import data
import random
from helpers import ask_input
import os

slot_1 = None
slot_2 = random.choice(data)
index = 1

score = 0
message = None
continue_game = True
while continue_game:
    print(logo)

    if message:
        print(message)

    slot_1, slot_2 = get_new_slots(slot_1, slot_2)

    print(f'Compare A: {format_data(slot_1)}')
    print(vs)
    print(f'Against B: {format_data(slot_2)}')

    guess = ask_input("Who has more followers? Type 'A' or 'B': ", valid_input)

    if correct_guess(guess, slot_1['follower_count'], slot_2['follower_count']):
        score += 1
        message = f"You're right! Current score {score}."
    else:
        continue_game = False
        message = f"Sorry, that's wrong. Final score {score}."

    os.system('clear')

print(logo)
print(message)
