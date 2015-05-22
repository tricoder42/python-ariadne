# coding: utf-8
from __future__ import unicode_literals

from attrdict import AttrDict


def splinter(driver_name='phantomjs', context=None):
    """
    Add splinter browser instance to context.

    :param driver_name: The name of browser to use:
                        phantomjs (default), firefox, chrome
    :param context: (optional) context to fill or manipulate
    :return: updated context with ``browser`` attribute
    """

    if not context:
        context = {}

    import splinter
    context.update({
        'browser': splinter.Browser(driver_name)
    })
    return AttrDict(context)
