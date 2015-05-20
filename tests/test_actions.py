# coding: utf-8
from __future__ import unicode_literals

import pytest
from mock import Mock
from attrdict import AttrDict

from ariadne.actions import Visit, Action


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

    def test_run(self, action):
        """
        Browser should visit given URL.
        """

        mock = Mock()
        context = AttrDict({
            'browser': mock
        })
        action.run(context)
        assert mock.visit.called_with('http://google.com')
