# coding: utf-8
from __future__ import unicode_literals

from attrdict import AttrDict

from . import Context


class Splinter(Context):
    """
    Add splinter browser instance and server_url to context.

    :param driver_name: The name of browser to use:
                        phantomjs (default), firefox, chrome
    """

    def __init__(self, driver_name='phantomjs'):
        self.driver_name = driver_name

    def __call__(self, context=None):
        if not context:
            context = {}

        import splinter
        context.update({
            'browser': splinter.Browser(self.driver_name),
            'server_url': 'http://localhost:8000',
        })
        return AttrDict(context)
