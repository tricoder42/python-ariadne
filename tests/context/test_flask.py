# coding: utf-8
from __future__ import unicode_literals

import logging
import pytest
from flask import Flask

from ariadne.context.flask import FlaskApp


@pytest.fixture(params=[200, 404])
def flask_app(request, caplog):
    # Disable flask server logging
    caplog.setLevel(logging.ERROR, 'werkzeug')

    app = Flask(__name__)
    if request.param == 200:
        # Add root handler to test that FlaskApp processor can detect running
        # flask app properly both with and without root handler.
        app.route('/')(lambda: 'Homepage')

    return app


@pytest.fixture
def processor(request, flask_app):
    app = FlaskApp(app=flask_app)
    request.addfinalizer(app.stop)
    return app


def test_get_free_port(processor):
    """ Should return free port as integer. """
    assert isinstance(processor.get_free_port(), int)


def test_start(processor):
    """ Should start server as separated process, listening at `port`. """
    processor.start()

    assert processor.port
    assert processor._process


def test_server_url(processor):
    """ Should return absolute URL to server. """
    server_url = 'http://localhost:80'
    assert processor.server_url == server_url

    processor.start()
    server_url = 'http://localhost:{0}'.format(processor.port)
    assert processor.server_url == server_url


def test_repr(processor):
    """ Should return object representation as string. """
    processor.start()

    expected = '<Flask app listening at {0}>'.format(processor.server_url)
    assert repr(processor) == expected


def test_processor(processor):
    ctx = processor()
    assert ctx.server_url == processor.server_url
