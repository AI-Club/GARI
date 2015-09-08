from unittest import TestCase

from gari.models import Object, Agent, Action
from gari.util import create_class


class TestModels(TestCase):

    def test_registry(self):
        """Dynamic class registry"""
        foo = create_class('Foo')
        bar = create_class('Bar')
        person = create_class('Person', class_type=Agent)
        eat = create_class('Eat', class_type=Action)

        self.assertIn(foo, Object.registry)
        self.assertIn(bar, Object.registry)
        self.assertNotIn(foo, Action.registry)
        self.assertNotIn(foo, Agent.registry)
        self.assertNotIn(bar, Action.registry)
        self.assertNotIn(bar, Agent.registry)

        self.assertIn(person, Agent.registry)
        self.assertNotIn(person, Object.registry)
        self.assertNotIn(person, Action.registry)

        self.assertIn(eat, Action.registry)
        self.assertNotIn(eat, Object.registry)
        self.assertNotIn(eat, Agent.registry)
