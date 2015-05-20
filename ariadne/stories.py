# coding: utf-8
from __future__ import unicode_literals


class Story(object):
    """ Base class for all stories """

    def __init__(self, actions):
        self.actions = actions

    def as_scenario(self):
        from ariadne.scenarios import Scenario
        return Scenario([self])


class Simple(Story):
    """ Run actions in series """
