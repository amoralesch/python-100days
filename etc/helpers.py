import smtplib
from typing import Callable
import os

SOURCE_EMAIL = os.environ.get('MY_EMAIL')
SOURCE_PASS = os.environ.get('MY_EMAIL_PASSWORD')
SMTP_SERVER = 'smtp-mail.outlook.com'
SMTP_PORT = 587


def is_yes_or_no(value: str) -> bool:
    return value.lower() == "yes" or value.lower() == "no"


def ask_input(
        prompt: str,
        validator: Callable[[str], bool],
        error_msg = "Invalid option, try again.") -> str:
    value = input(prompt)

    while not validator(value):
        print(error_msg)
        value = input(prompt)

    return value


def send_email(to_email: str, subject: str, message: str) -> None:
    with smtplib.SMTP(
            host=SMTP_SERVER,
            port=SMTP_PORT,
            timeout=30) as connection:
        connection.starttls()
        connection.login(user=SOURCE_EMAIL, password=SOURCE_PASS)
        connection.sendmail(
            from_addr=SOURCE_EMAIL,
            to_addrs=to_email,
            msg=f'Subject: {subject}\n\n{message}')
