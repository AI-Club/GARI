"""
Utility functions
"""

from .models import Object


def create_class(name, class_type=None, attrs=None):
    if class_type is None:
        class_type = Object
    if attrs is None:
        attrs = {}
    return type(name, (class_type,), attrs)
