import random
import requests
from requests import HTTPError
from account import Account

PIXELA_USER_API_ENDPOINT = 'https://pixe.la/v1/users'
PIXELA_USER_PARAMS = {
    'token': 'token',
    'username': 'username',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}


def new_token() -> str:
    """Valid regex: [ -~]{8,128}"""
    minimum = ord(' ')
    maximum = ord('~')
    token = ''
    length = random.randint(8, 128)

    for _ in range(length):
        token += chr(random.randint(minimum, maximum))

    print(token)
    return token


def create_user(account) -> bool:
    params = PIXELA_USER_PARAMS
    params['token'] = account.token
    params['username'] = account.username

    response = requests.post(url=PIXELA_USER_API_ENDPOINT, json=params)

    try:
        response.raise_for_status()
        return True
    except HTTPError:
        return False


def delete_account(account: Account) -> bool:
    headers = {
        'X-USER-TOKEN': account.token
    }

    response = requests.delete(
        url=f'{PIXELA_USER_API_ENDPOINT}/{account.username}',
        headers=headers)

    try:
        response.raise_for_status()
    except HTTPError:
        return False

    return True


class PixelaManager:
    def __init__(self):
        pass
