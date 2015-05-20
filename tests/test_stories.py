# coding: utf-8
from __future__ import unicode_literals

from ariadne.scenarios import Scenario
from ariadne.stories import Story


def test_story_as_scenario():
    story = Story([])
    scenario = story.as_scenario()
    assert isinstance(scenario, Scenario)
    assert story in scenario.stories
