"""
Person model
"""

import random

from .base import Object, Action


class Person(Object):

    """Model for person objects"""

    attributes = ['health', 'food', 'energy']
    actions = ['eat', 'sleep', 'run']

    def action_eat(self, recv):


class Food(Object):

    """Model food objects"""

    name = "eat"

    def when_eat(self, actor):
        actor.energy += random.choice(xrange(5, 10))
