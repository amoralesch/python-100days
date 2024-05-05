# Habit Tracker

# Create a habit tracker, using [Pixela](pixe.la) as the back-end.
#
# Lear about other HTTP verbs, `POST, `PUT`, and `DELETE`

from etc.helpers import ask_input
from account_manager import AccountManager
from account import Account
from pixela_manager import new_token, create_user, delete_account


def is_valid(selection: str) -> bool:
    return selection.isnumeric() and 0 < int(selection) < 10


def valid_username(selection: str) -> bool:
    """Valid regex: [a-z][a-z0-9-]{1,32}"""
    valid = selection[0:1].isalpha()

    for char in selection[1:]:
        valid = valid and char.isalnum()

    return valid and 0 < len(selection) <= 32


def get_option() -> int:
    print('What do you want to do?')
    print(' 1. View list of accounts.')
    print(' 2. Register a new account.')
    print(' 3. Remove an account.')
    print(' 4. Create a new graph.')
    print(' 5. Remove a graph.')
    print(' 6. Add a new pixel.')
    print(' 7. Edit a pixel.')
    print(' 8. Remove a pixel.')
    print(' 9. Exit.')

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
    else:
        restart = False
