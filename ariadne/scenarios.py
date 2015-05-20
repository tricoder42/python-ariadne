# coding: utf-8
from __future__ import unicode_literals


class Scenario(object):
    """ Base class for all scenarios """

    def __init__(self, stories):
        self.stories = stories
