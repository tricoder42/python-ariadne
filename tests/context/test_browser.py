# coding: utf-8
from __future__ import unicode_literals

from splinter.driver.webdriver import BaseWebDriver

from ariadne.context.browsers import Splinter


def test_splinter():
    """
    Create browser instance, which is phantomJS by default.
    """

    preprocessor = Splinter()
    context = preprocessor()
    assert 'browser' in context
    assert isinstance(context.browser, BaseWebDriver)
    assert context.browser.driver_name == 'PhantomJS'

    assert context.server_url == 'http://localhost:8000'
