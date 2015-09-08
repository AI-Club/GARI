from unittest import TestCase

from six import StringIO

from gari.environment import Environment
from gari.models import Object


class TestEnvironment(TestCase):

    def test_load(self):
        """Load definition data"""
        env = Environment()
        env.load_definitions()
        cls = [c for c in Object.registry
               if c.name == 'potato'][0]
        self.assertTrue(cls.calories, 300)
