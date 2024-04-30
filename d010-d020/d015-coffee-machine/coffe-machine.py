# Coffee Machine Program

# Build the software for a coffee machine, it should ask the type of
# coffee, ask the user to pay, check the price (and give change if
# needed), check if it has enough ingredients, and have an "off" and a
# "report" functionality

# Again, no new topic here, just an exercise to code from scratch and
# without hints.

from art import logo
from etc.helpers import ask_input

MENU = {
    'espresso': {
        'Water': 50,
        'Coffee': 18,
        'price': 1.5
    },
    'latte': {
        'Water': 200,
        'Milk': 150,
        'Coffee': 24,
        'price': 2.5
    },
    'cappuccino': {
        'Water': 250,
        'Milk': 100,
        'Coffee': 24,
        'price': 3
    }
}


def is_valid_option(value):
    v = value.strip().lower()
    valid_options = ['espresso', 'latte', 'cappuccino', 'off', 'report']

    return v in valid_options


def is_decimal(value):
    return value.strip().isdecimal()


def print_report():
    for item in resources:
        print(f"{item['name']}: {item['amount']}{item['unit']}")

    print(f'Money: ${profits:.2f}')


def enough_resources(r):
    for resource in resources:
        ingredient = resource['name']
        quantity = resource['amount']

        if ingredient in r and r[ingredient] > quantity:
            print(f'Sorry there is not enough {ingredient}.')

            return False

    return True


def make_coffee(r):
    for resource in resources:
        ingredient = resource['name']

        if ingredient in r:
            resource['amount'] -= r[ingredient]


def ask_money(money_name, value):
    msg = f'How many {money_name} did you inserted? '

    return int(ask_input(msg, is_decimal)) * value


profits = 0
resources = [
    {
        'name': 'Water',
        'amount': 300,
        'unit': 'ml'
    },
    {
        'name': 'Milk',
        'amount': 200,
        'unit': 'ml'
    },
    {
        'name': 'Coffee',
        'amount': 100,
        'unit': 'g'
    }
]

print(logo)
still_on = True

while still_on:
    option = ask_input(
        'What would you like? (espresso/latte/cappuccino): ',
        is_valid_option).lower()

    if option == 'off':
        still_on = False
    elif option == 'report':
        print_report()
    else:
        recipe = MENU[option]
        price = recipe['price']

        if not enough_resources(recipe):
            continue

        print(f'The price of {option} is ${price:.2f}.')
        
        amount = ask_money('quarters', 0.25)
        if amount < price:
            amount += ask_money('dimes', 0.10)
        if amount < price:
            amount += ask_money('nickles', 0.05)
        if amount < price:
            amount += ask_money('pennies', 0.01)
            
        if price > amount: 
            print("Sorry that's not enough money. Money refunded.")
            continue

        profits += price

        if amount > price:
            print(f'Here is ${(amount - price):.2f} dollars in change.')

        make_coffee(recipe)

        print(f'“Here is your {option}. Enjoy!”')
