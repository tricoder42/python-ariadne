# coding: utf-8
from __future__ import unicode_literals

from contextlib import contextmanager


class BaseConfig(object):
    @contextmanager
    def context(self):
        yield self.context_setup()
        self.context_teardown()

    def context_processors(self):
        return []

    def context_setup(self):
        context = {}
        for processor in self.context_processors():
            context = processor(context=context) or context
        return context

    def context_teardown(self):
        pass
