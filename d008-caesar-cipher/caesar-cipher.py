# Caesar Cipher
# Learn about defining functions with and without parameters, assign
# parameters by position or by name, default values for parameters, and
# return values.

from art import logo
from verify import validChoice, isEncodeOrDecode, isYesOrNo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(starting_text, shift_amount, operation):
    ending_text = ""

    if operation == "decode":
        shift_amount *= -1

    for char in starting_text:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + shift_amount) % len(alphabet)
            ending_text += alphabet[new_index]
        else:
            ending_text += char

    print(f"Your {operation}d text is {ending_text}")

print(logo)
print("Welcome to Caesar Cipher.")

end_program = False

while not end_program:
    operation = validChoice("Type 'encode' to encode a text, or 'decode' to decode it.\n",
        isEncodeOrDecode)

    text = input("Write the text.\n").lower()
    shift = int(input("Type the shift number.\n"))

    caesar_cipher(operation=operation, starting_text=text, shift_amount=shift)

    option = validChoice("Do you want to do it again? Type 'yes' or 'no'\n",
        isYesOrNo, "Pay attention! That is not a valid choice.")

    if option == 'no':
        end_program = True
        print("Goodbye.")
