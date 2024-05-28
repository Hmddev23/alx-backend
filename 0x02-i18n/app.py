#!/usr/bin/env python3
"""
A Flask web application with Babel for internationalization
user-specific settings, and timezone handling.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


class Config(object):
    """
    set the default locale, timezone, and supported languages
    for the Babel extension.
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.timezoneselector
def get_timezone() -> str:
    """
    check if the 'timezone' query parameter is present and valid,
    otherwise falls back to the user's preferred timezone.
    Returns:
        str: The appropriate timezone string.
    """
    try:
        if request.args.get("timezone"):
            return pytz.timezone(request.args.get("timezone")).zone
        if g.user and g.user.get("timezone"):
            return pytz.timezone(g.user["timezone"]).zone
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    return "UTC"


def get_user() -> dict:
    """
    retrieve a user dictionary based on the 'login_as' query parameter.
    Returns:
        dict: The user dictionary if found, otherwise None.
    """
    user_id = request.args.get("login_as")
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request() -> None:
    """
    call `get_user` to fetch the user data based on the
    'login_as' query parameter and assigns it to `g.user` for use
    in the request context.
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    select the best match for supported languages based on the request.
    Returns:
        str: The best match for the client's preferred language.
    """
    if request.args.get("locale") in app.config["LANGUAGES"]:
        return request.args.get("locale")
    if g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user["locale"]
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """
    render and returns the "index.html" template along with the
    current time formatted according to the user's locale and timezone.
    Returns:
        str: The rendered HTML template.
    """
    from datetime import datetime
    from flask_babel import format_datetime

    current_time = format_datetime(datetime.utcnow())
    return render_template("index.html", current_time=current_time)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
