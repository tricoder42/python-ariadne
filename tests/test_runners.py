# coding: utf-8
from __future__ import unicode_literals

import pytest

from ariadne.config import BaseConfig
from ariadne.runners import SimpleRunner
from ariadne.scenarios import Scenario


def test_config_default():
    """ When no config is specified, BaseConfig is taken """
    runner = SimpleRunner()
    assert isinstance(runner.config, BaseConfig)


def test_config_invalid():
    """ Invalid config should raise ValueError """
    with pytest.raises(ValueError):
        SimpleRunner(config=object)

    with pytest.raises(ValueError):
        SimpleRunner(config=BaseConfig())


def test_add():
    """ Add Scenario to runner """
    scenario = Scenario([])

    runner = SimpleRunner()
    assert not runner.scenarios

    runner.add(scenario)
    assert scenario in runner.scenarios
