# coding: utf-8
from __future__ import unicode_literals


class BaseConfig(object):
    def context_processors(self):
        return []

    def context_setup(self):
        context = {}
        for processor in self.context_processors():
            context = processor(context=context) or context
        return context
