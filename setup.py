'''
Good Agent-based Romcom Intelligence
'''

import sys
from setuptools import setup, find_packages


setup(
    name='gari',
    version='0.1',
    license='BSD',
    description='',
    packages=find_packages(),
    package_data={
        '': ['gari/definitions/*.yaml']
    },
    long_description=sys.modules[__name__].__doc__,
    include_package_data=True,
    install_requires=['six', 'pyyaml'],
)
