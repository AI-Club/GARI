"""
Environment models
"""

import six

from .meta import RegistryMeta


class Base(object):

    """Base for model :py:cls:`Object` and :py:cls:`Agent` classes"""

    name = None
    attributes = []
    actions = []
    children = []
    parent = None

    def __str__(self):
        return '{0} {1}'.format(self.name, self.__class__.__name__.lower())


@six.add_metaclass(RegistryMeta)
class Object(Base):

    """Model for objects"""

    pass


@six.add_metaclass(RegistryMeta)
class Agent(Base):

    """Agents are special objects"""

    def update(self):
        """Update goals and agent observations"""
        pass

    def update_knowledge(self):
        """Update agent knowledge of objects"""
        for obj in self.child_objects:
            self.observe(obj)

    def observe(self, obj):
        """Observe object"""
        pass


@six.add_metaclass(RegistryMeta)
class Action(Base):

    """Model for actions between :py:cls:`Object` instances"""

    pass
