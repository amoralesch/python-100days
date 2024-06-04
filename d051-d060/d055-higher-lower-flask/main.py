# High or Lower - Web Version

# Re-create the game _Higher or Lower_ (from day 14), but this time one
# a web browser
#
# Learn about Flask, and decorators

from flask import Flask
import random

HINTS = True
CORRECT_HASH = '4T7e4DmcrP9du'
HIGH_HASH = '3o6ZtaO9BZHcOjmErm'
LOW_HASH = 'jD4DwBtqPXRXa'

app = Flask(__name__)
number = random.randint(1, 10)


def hint_decorator(function):
    def wrapper(**kwargs):
        msg = function(**kwargs)

        if HINTS:
            msg += f"<br />Pst, the number is {number}."

        return msg

    wrapper.__name__ = function.__name__

    return wrapper


def alert_decorator_factory(color: str, image_hash: str):
    def alert_decorator(function):
        def wrapper():
            msg = \
                f'<div style="color:{color}"><h2>{function()}</h2></div>' \
                f'<img src="https://media.giphy.com/media/{image_hash}/giphy.gif" />'

            return msg

        wrapper.__name__ = function.__name__

        return wrapper

    return alert_decorator


@app.route('/')
@hint_decorator
def home_page():
    msg = \
        "<h1>Guess my number!</h1>" \
        "<p>I'm thinking of a number between 1 and 10 (inclusive).<br />" \
        "Try to guess it in as few attempts as you can.<br />" \
        "Change the URL to include the number at the end, i.e. `/50`.</p>" \
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" />'

    return msg


@app.route('/<int:guess>')
@hint_decorator
def guess_number(guess):
    if guess == number:
        msg = correct()
    elif guess < number:
        msg = too_low()
    else:
        msg = too_high()

    return msg


@alert_decorator_factory('red', HIGH_HASH)
def too_high():
    return 'Too high.'


@alert_decorator_factory('yellow', LOW_HASH)
def too_low():
    return 'Too Low.'


@alert_decorator_factory('green', CORRECT_HASH)
def correct():
    return 'Correct.'


if __name__ == '__main__':
    app.run(port=8080, debug=True)
