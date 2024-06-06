# Name Card Website

# Create a website, using a template from HTML5UP, and serve it using
# Flask.
#
# Learn about using templates and static resources in Flask.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
