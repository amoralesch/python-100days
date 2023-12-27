# Calculator

# Learn about functions with and without parameters, functions with return
# values, and dictionaries.

from art import logo
import os

def add(first, second):
    return first + second

def minus(first, second):
    return first - second

def multiply(first, second):
    return first * second

def divide(first, second):
    return first / second

operations = {
    '+': add,
    '-': minus,
    '*': multiply,
    '/': divide
}

finish = False

while not finish:
    print(logo)

    number_1 = float(input("What's the first number?: "))

    for key in operations:
        print(key)

    restart = False

    while not restart:
        op = input("Pick an operation: ")

        number_2 = float(input("What's the next number?: "))
        result = operations[op](number_1, number_2)

        print(f"{number_1} {op} {number_2} = {result}")

        selection = input(f"Type 'y' to continue calculating with {result}, " +
            "'n' to start a new calculation, or 'x' to exit: ").lower()

        finish = selection == 'x'
        restart = selection == 'n' or finish
        number_1 = result

    if not finish:
        os.system('clear')
