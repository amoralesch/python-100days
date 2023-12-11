# PyPassword Generator (version 2)

# Learn about while loops

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+']
all_options = [letters, numbers, symbols]

print("Welcome to PyPassword Generator.")

number_letters = int(input("Who many letters would you like in your password?\n"))
number_symbols = int(input("Who many symbosl would you like?\n"))
number_numbers = int(input("Who many numbers would you like?\n"))

total_len = number_letters + number_symbols + number_numbers
selected = [number_letters, number_symbols, number_numbers]
password = ''

while len(password) < total_len:
    type = random.randint(0, 2)
    if selected[type] > 0:
        password += random.choice(all_options[type])
        selected[type] -= 1

print(f"Here is your password: {password}")
