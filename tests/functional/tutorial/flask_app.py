# coding: utf-8
from __future__ import unicode_literals

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "It works!"


@app.route("/login/")
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run()
