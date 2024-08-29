# Automatic Birthday Wisher

# Send an automatic email to people whose birthday is today.
#
# Learn about `timedate` and `smtplib` libraries.

import smtplib
import pandas
import datetime as dt
import random

SOURCE_EMAIL = 'update@email.com'
SOURCE_PASS = 'update_password'
SMTP_SERVER = 'smtp-mail.outlook.com'
SMTP_PORT = 587


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
            msg=f'Subject: Happy Birthday!\n\n{message}')


def get_letter():
    letter_name = f'data/letters/letter-{random.randint(1, 4)}.txt'

    with open(letter_name) as file:
        return file.read()


today = (dt.datetime.now().month, dt.datetime.now().day)
records = pandas.read_csv('data/birthdays.csv')

today_birthdays = {
    data['name']: data['email']
    for _, data in records.iterrows()
    if data['month'] == today[0] and data['day'] == today[1]
}

for (name, email) in today_birthdays.items():
    letter_template = get_letter()
    letter = letter_template.replace('[name]', name)
    send_email(email, letter)
