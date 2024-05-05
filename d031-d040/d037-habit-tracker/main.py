# Habit Tracker

# Create a habit tracker, using [Pixela](pixe.la) as the back-end.
#
# Lear about other HTTP verbs, `POST, `PUT`, and `DELETE`

from etc.helpers import ask_input
import random
import pandas
import requests


def is_valid(selection: str) -> bool:
    return selection.isnumeric() and 0 < int(selection) < 10


def valid_username(selection: str) -> bool:
    """Valid regex: [a-z][a-z0-9-]{1,32}"""
    valid = selection[0:1].isalpha()

    for char in selection[1:]:
        valid = valid and char.isalnum()

    return valid and 0 < len(selection) <= 32


def new_token() -> str:
    """Valid regex: [ -~]{8,128}"""
    minimum = ord(' ')
    maximum = ord('~')
    token = ''
    length = random.randint(8, 128)

    for _ in range(length):
        token += chr(random.randint(minimum, maximum))

    return token


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


def username_exists(username: str) -> bool:
    try:
        data = pandas.read_csv(CONFIG_FILE)

        return username in [row['NAME'] for _, row in data.iterrows()]
    except FileNotFoundError:
        return False


def store_account(username: str, token: str) -> None:
    try:
        data = pandas.read_csv(CONFIG_FILE)
        accounts = data.to_dict(orient='records')
    except FileNotFoundError:
        accounts = []

    accounts.append({
        'NAME': username,
        'TOKEN': token
    })

    df = pandas.DataFrame(accounts)
    df.to_csv(CONFIG_FILE, index=False)


def create_account() -> None:
    username = ask_input(
        "What's the username? [a-z][a-z0-9-]{1,32} ",
        valid_username)

    if username_exists(username):
        print('That username already exists.')

        return

    token = new_token()

    params = PIXELA_USER_PARAMS
    params['token'] = token
    params['username'] = username

    response = requests.post(url=PIXELA_USER_API_ENDPOINT, json=params)
    response.raise_for_status()

    store_account(username, token)
    print(f'Account created, go to: https://pixe.la/@{username}')


CONFIG_FILE = 'output/accounts.csv'

PIXELA_USER_API_ENDPOINT = 'https://pixe.la/v1/users'
PIXELA_USER_PARAMS = {
    'token': 'token',
    'username': 'username',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

restart = True

while restart:
    option = get_option()

    if option == 1:
        show_accounts()
    elif option == 2:
        create_account()
    else:
        restart = False
