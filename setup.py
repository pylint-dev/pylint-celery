# -*- coding: UTF-8 -*-
from distutils.core import setup
from setuptools import find_packages

_version = "0.3"
_packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

_short_description = "pylint-celery is a Pylint plugin to aid Pylint in recognising and understanding" \
                     "errors caused when using the Celery library"


setup( name='pylint-celery',
       url='https://github.com/landscapeio/pylint-celery',
       author='landscape.io',
       author_email='code@landscape.io',
       description=_short_description,
       version=_version,
       packages=_packages,
       install_requires=['pylint>=1.0', 'astroid>=1.0', 'pylint-plugin-utils>=0.2.1'],
       license='GPLv2',
       keywords='pylint celery plugin',
       zip_safe=False,  # https://github.com/landscapeio/prospector/issues/18#issuecomment-49857277
       classifiers=(
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
        )
)
