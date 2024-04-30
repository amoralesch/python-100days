import requests
import datetime as dt
import math

# Update to your location
OUR_LOCATION = {
    "latitude": 40.728157,
    "longitude": -74.077644
}
TIME_ZONE = 'America/New_York'
TIME_API_URL = 'https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&tzid={timezone}&formatted=0'
ISS_URL = 'http://api.open-notify.org/iss-now.json'
ISS_json_file = requests.get(ISS_URL)
ISS_lat = ISS_json_file.json()['iss_position']['latitude']
ISS_long = ISS_json_file.json()['iss_position']['longitude']

print(OUR_LOCATION['longitude'])
print(ISS_long)
print('------')
print(OUR_LOCATION['latitude'])
print(ISS_lat)

if (math.fabs(OUR_LOCATION['longitude'] - float(ISS_long)) <= 5 or
    math.fabs(OUR_LOCATION['latitude'] - float(ISS_lat)) <= 5):
    print("Look up!☝")
else:
    print("Don't look up")



def is_night_right_now():
    # find out if it is day or night in our location
    url = TIME_API_URL.replace(
        '{latitude}',
        str(OUR_LOCATION['latitude']))
    url = url.replace(
        '{longitude}',
        str(OUR_LOCATION['longitude']))
    url = url.replace(
        '{timezone}',
        TIME_ZONE)
    info = requests.get(url=url)
    sunrise = int(info.json()['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(info.json()['results']['sunset'].split('T')[1][0:2])
    hour_now = dt.datetime.now().hour

    return hour_now < sunrise or hour_now > sunset

# find out where the ISS is

# if it is night, and the ISS is above us, then
# send email
