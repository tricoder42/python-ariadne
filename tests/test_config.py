# coding: utf-8
from __future__ import unicode_literals

from mock import patch

from ariadne.config import BaseConfig


def simple_context(context):
    context.update({'simple': 'context'})
    return context


class ProcessorsConfig(BaseConfig):
    def context_processors(self):
        return [simple_context]


class TestConfig:
    def test_context_setup_empty(self):
        """ Context is empty by default. """

        config = BaseConfig()
        assert config.context_setup() == {}

    def test_context_setup_simple(self):
        """ Test context from single context processor """

        config = ProcessorsConfig()
        assert config.context_setup() == {'simple': 'context'}

    def test_context_as_contextmanager(self):
        """
        Test that BaseConfig.context() behaves like contextmanager. It runs
        context_setup() on enter and context_teardown() on exit.
        """

        config = BaseConfig()
        patch_setup = lambda: patch.object(config, 'context_setup')
        patch_teardown = lambda: patch.object(config, 'context_teardown')

        # Python2.6 doesn't support nested with-statement
        with patch_setup() as start:
            with patch_teardown() as stop:
                assert not start.called
                assert not stop.called

                with config.context() as ctx:
                    assert start.called
                assert stop.called