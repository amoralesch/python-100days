# Habit Tracker

# Create a habit tracker, using [Pixela](pixe.la) as the back-end.
#
# Lear about other HTTP verbs, `POST, `PUT`, and `DELETE`

from etc.helpers import ask_input
from account_manager import AccountManager
from account import Account
from graph import Graph
from pixela_manager import (
    new_token, create_user, delete_account, create_graph, get_graphs,
    get_graph, delete_graph, create_pixel, get_pixel, edit_pixel,
    delete_pixel)


def is_valid(selection: str) -> bool:
    return selection.isnumeric() and 0 <= int(selection) < 10


def valid_username(selection: str) -> bool:
    """Valid regex: [a-z][a-z0-9-]{1,32}"""
    valid = selection[0:1].isalpha()

    for char in selection[1:]:
        valid = valid and char.isalnum()

    return valid and 0 < len(selection) <= 32


def valid_graph_name(selection: str) -> bool:
    """Valid regex: ^[a-z][a-z0-9-]{1,16}"""
    valid = selection[0:1].isalpha()

    for char in selection[1:]:
        valid = valid and (char.isalnum() or char == '-')

    return valid and 0 < len(selection) <= 16


def valid_date(value: str) -> bool:
    """Format: yyyyMMdd"""
    return value.isnumeric() and len(value) == 8


def get_option() -> int:
    print('What do you want to do?')
    print(' 1. View list of accounts.')
    print(' 2. Register a new account.')
    print(' 3. Remove an account.')
    print(' 4. List existing graphs.')
    print(' 5. Create a new graph.')
    print(' 6. Remove a graph.')
    print(' 7. Add a new pixel.')
    print(' 8. Edit a pixel.')
    print(' 9. Remove a pixel.')
    print(' 0. Exit.')

    return int(ask_input('Select an option: ', is_valid))


def show_accounts() -> None:
    if len(account_manager.accounts) > 0:
        print('Accounts:')

        for a in account_manager.accounts:
            print(f'- {a.username}')
    else:
        print('No accounts found.')


def create_account() -> None:
    username = ask_input(
        "What's the username? [a-z][a-z0-9-]{1,32} ",
        valid_username)

    if account_manager.account_exists(username):
        print('That username already exists.')

        return

    account = Account(username, new_token())

    if create_user(account):
        account_manager.store_account(account)
        print(f'Account created, go to: https://pixe.la/@{username}')
    else:
        print('Unable to create account. Maybe try another username?')


def remove_account():
    username = input("What's the username? ")
    user = account_manager.get_account(username)

    if user is None:
        print('Username not found.')

        return

    if delete_account(user):
        account_manager.remove_account(user)
        print('Account deleted.')
    else:
        print('Some error occurred, please try again.')


def show_graphs():
    username = input("What's the username? ")
    user = account_manager.get_account(username)

    if user is None:
        print('Username not found.')

        return

    graphs = get_graphs(user)
    if len(account_manager.accounts) > 0:
        print('Graphs:')

        for g in graphs:
            print(f'- {g.id} -- {g.name}')
    else:
        print('No graphs found.')


def new_graph():
    username = input("What's the username? ")
    user = account_manager.get_account(username)

    if user is None:
        print('Username not found.')

        return

    graph_name = ask_input(
        "What's the graph name? ^[a-z][a-z0-9-]{1,16} ",
        valid_graph_name)
    unit = input("What's the unit? ")
    graph_type = input("What's the type? int | float: ")
    color = input("What's the color? shibafu | momiji | sora | ichou | ajisai | kuro: ")

    graph = Graph(
        graph_name,
        graph_name,
        unit,
        graph_type,
        color)

    if create_graph(user, graph):
        print('Graph created.')
    else:
        print('Error creating graph, maybe change graph name.')


def remove_graph():
    username = input("What's the username? ")
    user = account_manager.get_account(username)

    if user is None:
        print('Username not found.')

        return

    graph_id = input("What's the graph id? ")
    graph = get_graph(user, graph_id)

    if graph is None:
        print('Graph not found.')

        return

    if delete_graph(user, graph):
        print('Graph deleted.')
    else:
        print('Error deleting graph.')


def add_pixel():
    username = input("What's the username? ")
    user = account_manager.get_account(username)

    if user is None:
        print('Username not found.')

        return

    graph_id = input("What's the graph id? ")
    graph = get_graph(user, graph_id)

    if graph is None:
        print('Graph not found.')

        return

    date = ask_input("What's the date? [yyyyMMdd] ", valid_date)
    quantity = input("What's the quantity? ")

    if create_pixel(user, graph, date, quantity):
        print('Pixel added.')
    else:
        print('Error adding pixel.')


def change_pixel():
    username = input("What's the username? ")
    user = account_manager.get_account(username)

    if user is None:
        print('Username not found.')

        return

    graph_id = input("What's the graph id? ")
    graph = get_graph(user, graph_id)

    if graph is None:
        print('Graph not found.')

        return

    date = ask_input("What's the date? [yyyyMMdd] ", valid_date)

    pixel = get_pixel(user, graph, date)

    if pixel is None:
        print('Pixel not found.')

        return

    quantity = input("What's the new quantity? ")

    if edit_pixel(user, graph, date, quantity):
        print('Pixel changed.')
    else:
        print('Error changing pixel.')


def remove_pixel():
    username = input("What's the username? ")
    user = account_manager.get_account(username)

    if user is None:
        print('Username not found.')

        return

    graph_id = input("What's the graph id? ")
    graph = get_graph(user, graph_id)

    if graph is None:
        print('Graph not found.')

        return

    date = ask_input("What's the date? [yyyyMMdd] ", valid_date)

    pixel = get_pixel(user, graph, date)

    if pixel is None:
        print('Pixel not found.')

        return

    if delete_pixel(user, graph, date):
        print('Pixel deleted.')
    else:
        print('Error deleting pixel.')


account_manager = AccountManager()
restart = True

while restart:
    option = get_option()

    if option == 1:
        show_accounts()
    elif option == 2:
        create_account()
    elif option == 3:
        remove_account()
    elif option == 4:
        show_graphs()
    elif option == 5:
        new_graph()
    elif option == 6:
        remove_graph()
    elif option == 7:
        add_pixel()
    elif option == 8:
        change_pixel()
    elif option == 9:
        remove_pixel()
    else:
        restart = False
