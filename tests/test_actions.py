# coding: utf-8
from __future__ import unicode_literals

import pytest
from mock import Mock
from attrdict import AttrDict

from ariadne.actions import Visit, Action, FillForm


@pytest.fixture
def ctx_browser():
    """
    :return: Context with mocked browser.
    """

    mock = Mock()
    context = AttrDict({
        'browser': mock
    })
    return context


def test_action_run_not_implemented():
    """
    Run method isn't implemented in base class.
    """

    with pytest.raises(NotImplementedError):
        context = {}
        Action().run(context)


class TestVisit:
    @pytest.fixture
    def action(self):
        return Visit('http://google.com')

    def test_get_url(self, action):
        """
        get_url should return target URL.
        """

        assert action.get_url() == 'http://google.com'

    def test_run(self, action, ctx_browser):
        """
        Browser should visit given URL.
        """

        action.run(ctx_browser)
        assert ctx_browser.browser.visit.called_with('http://google.com')


class TestFillForm:
    @property
    def params(self):
        return {
            'username': 'admin',
            'password': 'secret',
        }

    def test_run(self, ctx_browser):
        action = FillForm(data=self.params)
        action.run(context=ctx_browser)

        ctx_browser.browser.fill_form.assert_called_with(self.params)
        assert not ctx_browser.browser.find_by_css.called

    def test_run_submit(self, ctx_browser):
        action = FillForm(data=self.params, submit='#btn-submit')
        action.run(context=ctx_browser)

        # Assert mock
        ctx_browser.browser.fill_form.assert_called_with(self.params)
        ctx_browser.browser.find_by_css.assert_called_with('#btn-submit')

    def test_run_submit_true(self, ctx_browser):
        action = FillForm(data=self.params, submit=True)
        action.run(context=ctx_browser)

        # Assert mock
        ctx_browser.browser.fill_form.assert_called_with(self.params)
        ctx_browser.browser.find_by_css.assert_called_with('[type="submit"]')
