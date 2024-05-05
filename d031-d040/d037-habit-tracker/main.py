# Habit Tracker

# Create a habit tracker, using [Pixela](pixe.la) as the back-end.
#
# Lear about other HTTP verbs, `POST, `PUT`, and `DELETE`

from etc.helpers import ask_input
import pandas
import requests


def is_valid(selection: str) -> bool:
    return selection.isnumeric() and 0 < int(selection) < 10


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
    try:
        data = pandas.read_csv(CONFIG_FILE)
        print('Accounts:')

        for name in [row['NAME'] for _, row in data.iterrows()]:
            print(f'- {name}')
    except FileNotFoundError:
        print('No accounts saved.')


CONFIG_FILE = 'output/accounts.csv'

restart = True

while restart:
    option = get_option()

    if option == 1:
        show_accounts()
    else:
        restart = False
