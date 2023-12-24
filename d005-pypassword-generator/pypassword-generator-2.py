# PyPassword Generator (version 2)

# Learn about for loops and `random` methods`

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+']

print("Welcome to PyPassword Generator.")

number_letters = int(input("How many letters would you like in your password?\n"))
number_symbols = int(input("How many symbols would you like?\n"))
number_numbers = int(input("How many numbers would you like?\n"))

selected_chars = []

for i in range (0, number_letters):
    selected_chars.append(random.choice(letters))

for i in range (0, number_symbols):
    selected_chars.append(random.choice(symbols))

for i in range (0, number_numbers):
    selected_chars.append(random.choice(numbers))

random.shuffle(selected_chars)

password = ""
for char in selected_chars:
    password += char

print(f"Here is your password: {password}")
