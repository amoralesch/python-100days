import requests

API_URL = 'https://opentdb.com/api.php?amount=10&type=boolean'
PARAMETERS = {
    'amount': 10,
    'type': 'boolean'
}

response = requests.get(url=API_URL, params=PARAMETERS)
response.raise_for_status()
data = response.json()
question_data = data['results']
