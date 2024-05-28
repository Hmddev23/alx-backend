#!/usr/bin/env python3
"""
A simple Flask web application with
Babel for internationalization support.
"""

from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale():
    """
    determine the best match for the languages supported
    by the application (as specified in the configuration).
    Returns:
        str: The best match for the client's preferred language.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """
    render and returns the "2-index.html" template
    when a request is made to the root URL.
    Returns:
        str: The rendered HTML template.
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
