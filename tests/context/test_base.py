# coding: utf-8
from __future__ import unicode_literals
from ariadne.context import StaticContext


def test_static_context():
    processor = StaticContext(key='value')
    context = processor.run({})

    assert context['key'] == 'value'
