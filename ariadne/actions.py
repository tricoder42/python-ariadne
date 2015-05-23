# coding: utf-8
from __future__ import unicode_literals

from six.moves.urllib.parse import urljoin


class Action(object):
    """ Base class for all actions """

    def run(self, context):
        raise NotImplementedError()


class Visit(Action):
    """ Visit an URL in browser """

    def __init__(self, url=None):
        self.url = url

    def get_url(self, server_url=None):
        """
        Return target URL. May be predefined in subclass with dynamic behaviour.

        :param server_url: Root server URL with scheme and domain
        :return: URL to visit
        """

        if not server_url:
            return self.url

        return urljoin(server_url, self.url)

    def run(self, context):
        server_url = context.get('server_url')
        url = self.get_url(server_url)
        context.browser.visit(url)


class FillForm(Action):
    """
    Fill data in form and (optionally) submit form.
    """

    def __init__(self, data=None, submit=None):
        if data is None:
            data = {}
        self.data = data

        if submit is True:
            submit = '[type="submit"]'
        self.submit = submit

    def run(self, context):
        context.browser.fill_form(self.data)

        if self.submit:
            context.browser.find_by_css(self.submit).first.click()
