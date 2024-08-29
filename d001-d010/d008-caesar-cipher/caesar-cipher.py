# Caesar Cipher
# Learn about defining functions with and without parameters, assign
# parameters by position or by name, default values for parameters, and
# return values.

from art import logo
from etc.helpers import ask_input, is_yes_or_no

ALPHABET = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def is_encode_or_decode(value):
    return value == 'encode' or value == 'decode'


def caesar_cipher(starting_text, shift_amount, op):
    ending_text = ""

    if op == "decode":
        shift_amount *= -1

    for char in starting_text:
        if char in ALPHABET:
            index = ALPHABET.index(char)
            new_index = (index + shift_amount) % len(ALPHABET)
            ending_text += ALPHABET[new_index]
        else:
            ending_text += char

    print(f"Your {op}d text is {ending_text}")


print(logo)
print("Welcome to Caesar Cipher.")

end_program = False

while not end_program:
    operation = ask_input(
        "Type 'encode' to encode a text, or 'decode' to decode it.\n",
        is_encode_or_decode)

    text = input("Write the text.\n").lower()
    shift = int(input("Type the shift number.\n"))

    caesar_cipher(
        op=operation, starting_text=text, shift_amount=shift)

    option = ask_input(
        "Do you want to do it again? Type 'yes' or 'no'\n",
        is_yes_or_no,
        "Pay attention! That is not a valid choice.")

    if option == 'no':
        end_program = True
        print("Goodbye.")
