# coding: utf-8
from __future__ import unicode_literals

from ariadne import actions, stories, config, runners
from ariadne.context import browsers, flask

from . import flask_app


# Configuration
class ExampleConfig(config.BaseConfig):
    def context_processors(self):
        return [
            flask.FlaskApp(flask_app.app),
            browsers.Splinter('phantomjs')
        ]

# Action, stories, scenarios
visit_login = actions.Visit(url='/login/')

credentials = {
    'username': 'admin',
    'password': 'secret',
}
fill_credentials = actions.FillForm(data=credentials, submit='#btn-submit')

login_process = stories.Simple([
    visit_login,
    fill_credentials
])

user_login = login_process.as_scenario()

# Run it
runner = runners.SimpleRunner(config=ExampleConfig)
runner.add(user_login)
