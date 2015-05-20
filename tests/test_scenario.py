# coding: utf-8
from __future__ import unicode_literals

from mock import Mock

from ariadne.scenarios import Scenario


class TestScenario:
    def test_run(self):
        """
        Run method should run all stories defined in scenario and passed
        context if it's changed.
        """

        # Check that action was executed
        story = Mock(**{'run.return_value': None})
        scenarios = Scenario([story])
        assert scenarios.run() == {}
        assert story.run.called_with({})

        # Check that changed context is passed along
        changed_context = {'key': 'value'}
        story_side_effect = Mock(**{'run.return_value': changed_context})
        scenarios = Scenario([story_side_effect])
        assert scenarios.run() == changed_context
        assert story_side_effect.run.called_with({})

        # Check that context is kept intact when action doesn't return new one
        story.reset_mock()
        story_side_effect.reset_mock()
        scenarios = Scenario([
            story_side_effect,
            story
        ])
        assert scenarios.run() == changed_context
        assert story_side_effect.run.called_with({})
        assert story.run.called_with(changed_context)
