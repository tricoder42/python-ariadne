# coding: utf-8
from __future__ import unicode_literals


class Scenario(object):
    """ Base class for all scenarios """

    def __init__(self, stories):
        self.stories = stories

    def run(self):
        """
        Run all stories in scenario. Pass shared context through whole scenario.

        :return: context dictionary
        """

        context = {}

        for story in self.stories:
            context = story.run(context) or context
        return context
