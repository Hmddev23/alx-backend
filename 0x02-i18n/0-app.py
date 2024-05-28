#!/usr/bin/env python3
"""
serve a single HTML page.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """
    render and returns the "0-index.html" template
    when a request is made to the root URL.
    Returns:
        str: The rendered HTML template.
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
