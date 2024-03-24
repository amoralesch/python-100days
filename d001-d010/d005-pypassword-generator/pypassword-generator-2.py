# PyPassword Generator (version 2)

# Learn about for loops and `random` methods`

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+']
max_len = 10
warning = f"Enter a number between 0 and {max_len}"

print("Welcome to PyPassword Generator.")

number_letters = -1
while number_letters < 0 or number_letters > max_len:
    number_letters = int(input(f"How many letters would you like in your password? {warning}\n"))

number_symbols = -1
while number_symbols < 0 or number_symbols > max_len:
    number_symbols = int(input(f"How many symbols would you like? {warning}\n"))

number_numbers = -1
while number_numbers < 0 or number_numbers > max_len:
    number_numbers = int(input(f"How many numbers would you like? {warning}\n"))

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
