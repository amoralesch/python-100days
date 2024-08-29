import random
import requests
from requests import HTTPError
from account import Account
from graph import Graph

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


def get_graphs(account: Account) -> list[Graph]:
    headers = {
        'X-USER-TOKEN': account.token
    }

    response = requests.get(
        url=f'{PIXELA_USER_API_ENDPOINT}/{account.username}/graphs',
        headers=headers)

    try:
        response.raise_for_status()
    except HTTPError:
        return []

    return [
        Graph(g['id'], g['name'], g['unit'], g['type'], g['color'])
        for g in response.json()['graphs']]


def create_graph(account: Account, graph: Graph) -> bool:
    headers = {
        'X-USER-TOKEN': account.token
    }

    response = requests.post(
        url=f'{PIXELA_USER_API_ENDPOINT}/{account.username}/graphs',
        json=graph.to_dict(),
        headers=headers)

    try:
        response.raise_for_status()
    except HTTPError:
        return False

    return True


def get_graph(account: Account, graph_id: str) -> Graph | None:
    headers = {
        'X-USER-TOKEN': account.token
    }

    response = requests.get(
        url=f'{PIXELA_USER_API_ENDPOINT}/{account.username}/graphs/{graph_id}/graph-def',
        headers=headers)

    try:
        response.raise_for_status()
    except HTTPError:
        return None

    g = response.json()

    return Graph(g['id'], g['name'], g['unit'], g['type'], g['color'])


def delete_graph(account: Account, graph: Graph) -> bool:
    headers = {
        'X-USER-TOKEN': account.token
    }

    response = requests.delete(
        url=f'{PIXELA_USER_API_ENDPOINT}/{account.username}/graphs/{graph.id}',
        headers=headers)

    try:
        response.raise_for_status()
    except HTTPError:
        return False

    return True


def create_pixel(
        account: Account,
        graph: Graph,
        date: str,
        quantity: str):
    headers = {
        'X-USER-TOKEN': account.token
    }
    params= {
        'date': date,
        'quantity': quantity
    }

    response = requests.post(
        url=f'{PIXELA_USER_API_ENDPOINT}/{account.username}/graphs/{graph.id}',
        json=params,
        headers=headers)

    try:
        response.raise_for_status()
    except HTTPError:
        return False

    return True


def get_pixel(account: Account, graph: Graph, date: str) -> bool:
    headers = {
        'X-USER-TOKEN': account.token
    }

    response = requests.get(
        url=f'{PIXELA_USER_API_ENDPOINT}/{account.username}/graphs/{graph.id}/{date}',
        headers=headers)

    try:
        response.raise_for_status()

        return True
    except HTTPError:
        return False


def edit_pixel(account: Account, graph: Graph, date: str, quantity: str) -> bool:
    headers = {
        'X-USER-TOKEN': account.token
    }
    params = {
        'quantity': quantity
    }

    response = requests.put(
        url=f'{PIXELA_USER_API_ENDPOINT}/{account.username}/graphs/{graph.id}/{date}',
        json=params,
        headers=headers)

    try:
        response.raise_for_status()

        return True
    except HTTPError:
        return False


def delete_pixel(account: Account, graph: Graph, date: str) -> bool:
    headers = {
        'X-USER-TOKEN': account.token
    }

    response = requests.delete(
        url=f'{PIXELA_USER_API_ENDPOINT}/{account.username}/graphs/{graph.id}/{date}',
        headers=headers)

    try:
        response.raise_for_status()
    except HTTPError:
        return False

    return True


