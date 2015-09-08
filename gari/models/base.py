"""
Environment models
"""


class Model(object):

    """Base for model classes"""

    name = None

    def __str__(self):
        return self.name


class Action(Model):

    """Model for actions between :py:cls:`Person` instances"""

    pass


class Object(object):

    """Model for objects"""

    pass

