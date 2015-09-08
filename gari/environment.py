"""
Environment setup
"""

import os
import fnmatch

import yaml

from .util import create_class
from .models import Object, Agent, Action


class Environment(object):

    """Define environment and provide simulation"""

    def initialize(self):
        """Load environment"""
        self.load_definitions()

    def load_definitions(self):
        """Load definitions from YAML files"""
        path = os.path.join(os.path.dirname(__file__), 'definitions')
        for (dirpath, _, filenames) in os.walk(path):
            for filename in fnmatch.filter(filenames, '*.yaml'):
                with open(os.path.join(dirpath, filename)) as stream:
                    self.load_definition(stream)

    def load_definition(self, stream):
        """Load definition file

        :param stream: handle of file-like stream
        """
        objs = yaml.load(stream)
        if objs:
            for (name, attrs) in objs.items():
                class_type = Object
                try:
                    if attrs['type'] == 'action':
                        class_type = Action
                    if attrs['type'] == 'agent':
                        class_type = Agent
                except KeyError:
                    pass
                cls = create_class(name.title(), class_type=class_type)
                for (attr, value) in attrs.items():
                    setattr(cls, attr, value)
                cls.name = name
