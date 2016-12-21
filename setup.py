#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='train',
    version='0.0.1',
    description='Train',
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False,
    packages=find_packages(),
)

