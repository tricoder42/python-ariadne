# coding: utf-8
from __future__ import unicode_literals

from mock import Mock

from ariadne.scenarios import Scenario
from ariadne.stories import Story


class TestStory:
    def test_as_scenario(self):
        story = Story([])
        scenario = story.as_scenario()
        assert isinstance(scenario, Scenario)
        assert story in scenario.stories

    def test_run(self):
        """
        Run method should run all actions defined in story and passed
        context if it's changed.
        """

        # Check that action was executed
        context = {'hello': 'world'}
        action = Mock(**{'run.return_value': None})
        story = Story([action])
        assert story.run(context) == context
        assert action.run.called_with(context)

        # Check that changed context is passed along
        changed_context = {'key': 'value'}
        action_side_effect = Mock(**{'run.return_value': changed_context})
        story = Story([action_side_effect])
        assert story.run(context) == changed_context
        assert action_side_effect.run.called_with(context)

        # Check that context is kept intact when action doesn't return new one
        action.reset_mock()
        action_side_effect.reset_mock()
        story = Story([
            action_side_effect,
            action
        ])
        assert story.run(context) == changed_context
        assert action_side_effect.run.called_with(context)
        assert action.run.called_with(changed_context)

