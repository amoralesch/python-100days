# Weather Alert

# A program that will check the weather forecast, and alert a user when
# there may be rain in the next 15 hours.
#
# Originally planned to alert via SMS (using Twilio), but in the end
# decided to use email, as we cannot create a free Twilio account
# without a real phone number.
#
# More practice about APIs

import requests
import smtplib

CURRENT_LOCATION = {
    'latitude': 40.728157,
    'longitude': -74.077644
}
API_KEY = 'update-me'
WEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/forecast'
# taken from https://openweathermap.org/weather-conditions
ALERT_THRESHOLD = 700
WEATHER_PARAMS = {
    'lat': CURRENT_LOCATION['latitude'],
    'lon': CURRENT_LOCATION['longitude'],
    'appid': API_KEY,
    'units': 'metric',
    'cnt': 5
}
SOURCE_EMAIL = 'update-me'
SOURCE_PASS = "update-me"
SMTP_SERVER = 'smtp-mail.outlook.com'
SMTP_PORT = 587


def umbrella_needed():
    response = requests.get(url=WEATHER_API_URL, params=WEATHER_PARAMS)
    response.raise_for_status()

    data = response.json()
    weather_info = [
        item['weather'][0]['id']
        for item in data['list']
        if item['weather'][0]['id'] < ALERT_THRESHOLD]

    return len(weather_info) > 0


def send_alert():
    with smtplib.SMTP(
            host=SMTP_SERVER,
            port=SMTP_PORT,
            timeout=30) as connection:
        connection.starttls()
        connection.login(user=SOURCE_EMAIL, password=SOURCE_PASS)
        connection.sendmail(
            from_addr=SOURCE_EMAIL,
            to_addrs=SOURCE_EMAIL,
            msg="Subject: Bring an umbrella!\n\n"
                "Rain is forecasted, don't forget your umbrella!")


if umbrella_needed():
    print('Alert sent')
    send_alert()
