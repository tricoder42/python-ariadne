# coding: utf-8
from __future__ import unicode_literals
import sys

from ariadne.config import BaseConfig
from ariadne.scenarios import Scenario


class Runner(object):
    """ Base class for all runners. """


class SimpleRunner(Runner):
    def __init__(self, config=None):
        if config is None:
            config = BaseConfig
        elif isinstance(config, BaseConfig):
            msg = "You need to pass config class, not instance. Got {0}."
            raise ValueError(msg.format(config))
        elif not issubclass(config, BaseConfig):
            msg = "Config class must be derived from BaseConfig. Got {0}."
            raise ValueError(msg.format(config))

        self.config = config()
        self.scenarios = []

    def add(self, scenario):
        if not isinstance(scenario, Scenario):
            msg = "You need to add Scenario instances, got {0}."
            raise ValueError(msg.format(scenario))

        self.scenarios.append(scenario)

    def run(self):
        for scenario in self.scenarios:
            with self.config.context() as context:
                scenario.run(context)

