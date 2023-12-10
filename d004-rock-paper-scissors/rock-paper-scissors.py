# Rock-Paper-Scissors

# Learn about arrays and random numbers

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

print("Welcome to Rock-Paper-Scissors.")
user_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
print(options[user_option])

print("Computer chose:")
cpu_option = random.randint(0, 2)
print(options[cpu_option])

if user_option == cpu_option:
    print("It's a draw.")
elif (user_option + 1) % 3 == cpu_option:
    print("You lose.")
else:
    print("You won!")
