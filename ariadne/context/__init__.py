# coding: utf-8
from __future__ import unicode_literals

from attrdict import AttrDict


class Context(object):
    """ Base class for Context classes. """


class StaticContext(Context):
    """
    Add static data to context.

    .. code-block: python

       processor = StaticContext(key='value', secret='42')
       context = processor.run({})
       assert context == {'key': 'value', 'secret': 42}
    """

    def __init__(self, **kwargs):
        self.data = kwargs

    def run(self, context):
        context.update(self.data)
        return AttrDict(context)
