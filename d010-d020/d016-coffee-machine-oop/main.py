# Coffee Machine Program (OOP version)

# Redo the previous day exercise, but this time using OOP principles
#
# The classes and objects were created by the trainer, and this is the
# only file we need to implement. We are not allowed to modify the code
# in the other files.

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from etc.helpers import ask_input

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


def is_valid_option(value):
    v = value.strip().lower()
    valid_options = ['off', 'report', 'start']

    return v in valid_options or menu.find_drink(v) is not None


still_on = True

while still_on:
    option = ask_input(
        f"Start      OFF     Report\n",
        is_valid_option).lower()

    if option == 'off':
        still_on = False
    elif option == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        option = ask_input(
            f'What would you like? ({menu.get_items()}): ',
            is_valid_option).lower()

        recipe = menu.find_drink(option)

        if coffee_maker.is_resource_sufficient(recipe):
            print(f'The price of {recipe.name} is ${recipe.cost:.2f}.')

            if money_machine.make_payment(recipe.cost):
                coffee_maker.make_coffee(recipe)
