#!/usr/bin/env python3
"""
A simple Flask web application with
Babel for internationalization support.
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """
    configuration class for the Flask application.
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def index():
    """
    render and returns the "1-index.html" template
    when a request is made to the root URL.
    Returns:
        str: The rendered HTML template.
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
