# Python - 100 days of code

Repo with the code created while viewing the curse _100 Days of Code: The
Complete Python Pro Bootcamp for 2023_ in [Udemy](https://www.udemy.com/).

A folder is created for each day, and the final exercise is inside the
folder. A small description of the topics to learn are at the top of each
file.

## Configuration

In order to run some of the projects, is necessary to have accounts on 
some of the web applications that provide free access to their APIs.

Instructions on how to register and create the keys are not included 
here, but a quick google search should be enough to find the required
information.

Once the accounts are created, the following environment variables need
to be configured:

### Email

An Outlook / Hotmail account was used for the project, if yours is 
different, update the `SMTP_SERVER` and `SMTP_PORT` variables inside
`etc/helpers.py` file to match the correct ones for your provider.

Also, include the following 2 environment variables:

* `MY_EMAIL` - Your email account.
* `MY_EMAIL_PASSWORD` - Password for the email account.

### Spotify

* `SPOTIFY_CLIENT_ID` - Spotify client ID.
* `SPOTIFY_CLIENT_SECRET` - Spotify client secret.

### Open Weather Map

* `OWM_API_KEY` - API key.

### Nutritionix

* `NUTRITIONIX_CLIENT_ID` - Client ID.
* `NUTRITIONIX_API_KEY` - API key.

### News API

* `NEWS_API_KEY` -- API key.

### Alpha Vantage

* `AV_API_KEY` - API key.
