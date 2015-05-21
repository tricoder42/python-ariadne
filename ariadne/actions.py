# coding: utf-8
from __future__ import unicode_literals


class Action(object):
    """ Base class for all actions """

    def run(self, context):
        raise NotImplementedError()


class Visit(Action):
    """ Visit an URL in browser """

    def __init__(self, url=None):
        self.url = url

    def get_url(self):
        """
        Return target URL. May be predefined in subclass with dynamic behaviour.

        :return: URL to visit
        """

        return self.url

    def run(self, context):
        """
        Run action in context

        :param context:
        :return: (optional) context dictionary
        """

        context.browser.visit(self.get_url())
