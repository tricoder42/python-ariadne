# coding: utf-8
from __future__ import unicode_literals

from attrdict import AttrDict


class Splinter(object):
    """
    Add splinter browser instance to context.

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
            'browser': splinter.Browser(self.driver_name)
        })
        return AttrDict(context)
