# coding: utf-8
from __future__ import unicode_literals

import logging
import pytest
from flask import Flask

from ariadne.context.flask import FlaskApp


@pytest.fixture
def flask_app(caplog):
    # Disable flask server logging
    caplog.setLevel(logging.ERROR, 'werkzeug')
    return Flask(__name__)


@pytest.fixture
def processor(flask_app):
    return FlaskApp(app=flask_app)


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
    server_url = 'http://localhost:{}'.format(processor.port)
    assert processor.server_url == server_url


def test_repr(processor):
    """ Should return object representation as string. """
    processor.start()

    expected = '<Flask app listening at {}>'.format(processor.server_url)
    assert repr(processor) == expected


def test_processor(processor):
    ctx = processor()
    assert ctx.server_url == processor.server_url
