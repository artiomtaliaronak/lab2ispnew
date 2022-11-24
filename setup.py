#!/usr/bin/env python

from setuptools import setup

setup(
    name="serializer",
    version="1.0.0",
    setup_requires=["wheel"],
    install_requires=["pyyaml", "wheel"],
    packages=["serializers/", "."],
    entry_points={"console_scripts": "cu=console_util:main"},
)