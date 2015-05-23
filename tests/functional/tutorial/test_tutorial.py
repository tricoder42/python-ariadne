# coding: utf-8
from __future__ import unicode_literals

import pytest

from .scenario_user_login import runner


def test_user_login():
    # Test passes when run() doesn't raise any error
    runner.run()
