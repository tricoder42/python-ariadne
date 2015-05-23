# coding: utf-8
from __future__ import unicode_literals

from contextlib import contextmanager


class BaseConfig(object):
    def __init__(self):
        self._context_processors = []

    @contextmanager
    def context(self):
        yield self.context_setup()
        self.context_teardown()

    def context_processors(self):
        return []

    def context_setup(self):
        # Make instance copy of context processors, otherwise context_teardown
        # wouldn't terminate processors instantiated here
        self._context_processors = list(self.context_processors())

        context = {}
        for processor in self._context_processors:
            context = processor(context=context) or context
        return context

    def context_teardown(self):
        for processor in self._context_processors:
            processor.teardown()
        self._context_processors = []
