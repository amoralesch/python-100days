# Exercise Tracker

# Track exercise done, by writing the exercise in plain english, and use
# an use [Nutritionix](https://docx.syndigo.com/developers/docs/nutritionix-api-guide)
# API to convert that intro a standard format.
#
# Originally was planned to use Google Sheets for storing the info, and
# be able to run the code anywhere, but because you cannot create a
# Google account without a phone number, the data will be stored on a
# CSV file.
#
# Again, no new concepts nor ideas, just a way to practice again by
# building from scratch.

import datetime as dt
import os
import requests

API_ID = os.environ.get('NUTRITIONIX_CLIENT_ID')
API_KEY = os.environ.get('NUTRITIONIX_API_KEY')
RECORDS = 'output/info.csv'

AGE = 20
WEIGHT = 80  # Kilograms
HEIGHT = 160  # Centimeters

API_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
HEADERS = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY
}
PARAMS = {
    'query': '',
    'weight_kg': WEIGHT,
    'height_cm': HEIGHT,
    'age': AGE
}


def ensure_file():
    try:
        with open(RECORDS, 'r'):
            pass
    except FileNotFoundError:
        with open(RECORDS, 'w') as file:
            file.write('DATE,TIME,EXERCISE,DURATION,CALORIES\n')


def save_info(
        date: str,
        time: str,
        exercise: str,
        duration: str,
        calories: str):
    ensure_file()
    record = f'{date},{time},{exercise},{duration},{calories}'

    with open(RECORDS, 'a') as file:
        file.write(f'{record}\n')


query = input("What exercise did you do today? ")

params = PARAMS
params['query'] = query

response = requests.post(url=API_ENDPOINT, headers=HEADERS, json=params)
response.raise_for_status()
data = response.json()

exercise_record = data['exercises'][0]

save_info(
    dt.date.today().strftime('%Y-%m-%d'),
    dt.date.today().strftime('%H:%M'),
    exercise_record['user_input'],
    exercise_record['duration_min'],
    exercise_record['nf_calories']
)
