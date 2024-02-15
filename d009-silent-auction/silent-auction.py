# Silent Aucion

# Learn about dictionaries

from art import logo
import os

register = {}

print(logo)
print("Welcome to the secret auction program.")
name = input("What is your name?: \n")

from verify_v2 import verify,isGreaterthanZero
others = True



while others:
    user_bid = verify("What's your bid?: $" , isGreaterthanZero, "Invalid bid. Try again.")    

#    name = input("What is your name?: ")
#    bid = -1
#    while bid <= 0:
#        bid = int(input("What's your bid?: $"))
#
#        if bid <= 0:
#            print('Invalid bid. Try again.')
#
    register[name] = user_bid
    print(name)


    others = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    others = others.lower() == 'yes' 

    if others:
        os.system('clear')

winner = "no one"
highest_bid = 0


for key in register:
    if register[key] > highest_bid:
        winner = key
        highest_bid = register[key]

print(f"The winner is {winner} with a bid of ${highest_bid}.")
