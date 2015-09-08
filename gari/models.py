"""
Environment models
"""


class Base(object):

    """Base for model classes"""

    name = None

    def __str__(self):
        return self.name


class Action(Base):

    """Model for actions between :py:cls:`Person` instances"""

    pass


class Object(Base):

    """Model for objects"""

    child_objects = []


class Agent(Object):

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
