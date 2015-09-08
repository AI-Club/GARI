"""
Utility functions
"""

from .models import Object


def create_class(name, class_type=None, **kwargs):
    if class_type is None:
        class_type = Object
    return type(name, (class_type,), kwargs)
