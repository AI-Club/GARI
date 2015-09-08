"""
Meta classes for modeling
"""


class RegistryMeta(type):

    """Register class ancestors with model class"""

    def __new__(cls, name, bases, namespace):
        dyncls = super(RegistryMeta, cls).__new__(cls, name, bases, namespace)
        if not hasattr(dyncls, 'registry'):
            dyncls.registry = set()
        dyncls.registry.add(dyncls)
        dyncls.registry -= set(bases)
        return dyncls
