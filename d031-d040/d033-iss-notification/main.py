# ISS fly-by Notification

# Use public APIs to know where the International Space Station is
# and email the user when the ISS is above them, and it is nigh time.
#
# Learn about `requests` library, APIs, and practice with `smtplib`

import requests
import datetime as dt
import math
import smtplib

OUR_LOCATION = {
    "latitude": 40.728157,
    "longitude": -74.077644
}
TIME_ZONE = 'America/New_York'
TIME_API_URL = 'https://api.sunrise-sunset.org/json'
ISS_URL = 'http://api.open-notify.org/iss-now.json'

SOURCE_EMAIL = 'email@company.tld'
SOURCE_PASS = 'secretEmailPASSWORD!'
SMTP_SERVER = 'smtp-mail.outlook.com'
SMTP_PORT = 587


def iss_above():
    iss_json_file = requests.get(ISS_URL)
    position = iss_json_file.json()['iss_position']
    iss_lat = position['latitude']
    iss_long = position['longitude']

    if (math.fabs(OUR_LOCATION['longitude'] - float(iss_long)) <= 5 and
            math.fabs(OUR_LOCATION['latitude'] - float(iss_lat)) <= 5):
        return True
    else:
        return False


def get_hour_from_datetime(datetime):
    return int(datetime.split('T')[1][0:2])


def send_email(to_email, message):
    with smtplib.SMTP(
            host=SMTP_SERVER,
            port=SMTP_PORT,
            timeout=30) as connection:
        connection.starttls()
        connection.login(user=SOURCE_EMAIL, password=SOURCE_PASS)
        connection.sendmail(
            from_addr=SOURCE_EMAIL,
            to_addrs=to_email,
            msg=f'Subject: Friendly message!\n\n{message}')


def is_night_right_now():
    params = {
        'lat': OUR_LOCATION['latitude'],
        'lng': OUR_LOCATION['longitude'],
        'tzid': TIME_ZONE,
        'formatted': 0
    }
    info = requests.get(url=TIME_API_URL, params=params)
    sunrise = get_hour_from_datetime(info.json()['results']['sunrise'])
    sunset = get_hour_from_datetime(info.json()['results']['sunset'])
    hour_now = dt.datetime.now().hour

    return hour_now < sunrise or hour_now > sunset


if iss_above() and is_night_right_now():
    send_email(SOURCE_EMAIL, "ISS above. Look up.")
else:
    send_email(SOURCE_EMAIL, "Don't look up, nothing to see.")
