# coding: utf-8
from __future__ import unicode_literals


class Story(object):
    """ Base class for all stories """

    def __init__(self, actions):
        self.actions = actions

    def as_scenario(self):
        """
        Convert story into simple scenario with single story only.
        :return: Scenario
        """

        from ariadne.scenarios import Scenario
        return Scenario([self])

    def run(self, context):
        """
        Run all actions in story and pass context.

        :param context:
        :return: context dictionary
        """

        for action in self.actions:
            context = action.run(context) or context
        return context


class Simple(Story):
    """ Run actions in series """
