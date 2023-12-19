# Silent Aucion

# Learn about dictionaries

from art import logo
import os
register = {}

print(logo)
print("Welcome to the secret auction program.")

others = True

while others:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    register[name] = bid

    others = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    others = others.lower() == 'yes'

    if others:
        os.system('clear')

winner = ""
highest_bid = -1

for key in register:
    if register[key] > highest_bid:
        winner = key
        highest_bid = register[key]

print(f"The winner is {winner} with a bid of ${highest_bid}.")
