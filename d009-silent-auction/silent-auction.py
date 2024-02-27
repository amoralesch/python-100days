# Silent Aucion

# Learn about dictionaries

from art import logo
import verify_v2
import os

other_bidder = True
register = {}

print(logo)
print("Welcome to the secret auction program.")

while other_bidder:
    user_name = verify_v2.verify("What is your name?: \n",
        verify_v2.validUserName, "Invalid name. Try again.")
    user_bid = verify_v2.verify("What's your bid?: $" ,
        verify_v2.isGreaterthanZero, "Invalid bid. Try again.")

    register[user_name] = int(user_bid)

    other_bidder = verify_v2.verify("Are there any other bidders? Type 'yes' or 'no'.\n",
        verify_v2.YesOrNo, "Invalid bid. Try again.")

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
