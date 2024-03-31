# Silent Aucion

# Learn about dictionaries

from art import logo
from etc.helpers import (
    ask_input, is_valid_username,
    is_yes_or_no, is_greater_than_zero
)
import os

other_bidder = True
register = {}

print(logo)
print("Welcome to the secret auction program.")

while other_bidder:
    user_name = ask_input(
        "What is your name?: \n",
        is_valid_username,
        "Invalid name. Try again.")
    user_bid = ask_input(
        "What's your bid?: $" ,
        is_greater_than_zero,
        "Invalid bid. Try again.")

    register[user_name] = int(user_bid)

    other_bidder = ask_input(
        "Are there any other bidders? Type 'yes' or 'no'.\n",
        is_yes_or_no,
        "Invalid bid. Try again.")

    other_bidder = other_bidder.lower() == 'yes'

    if other_bidder:
        os.system('clear')

winner = "no one"
highest_bid = 0

for key in register:
    if register[key] > highest_bid:
        winner = key
        highest_bid = register[key]

print(f"The winner is {winner} with a bid of ${highest_bid}.")
