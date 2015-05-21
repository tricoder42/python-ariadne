# coding: utf-8
from __future__ import unicode_literals
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
