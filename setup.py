#!/usr/bin/env python
import os

import pkg_resources
from setuptools import find_packages, setup

setup(
    name="MTL",
    version="0.0.1",
    description="Towards efficient recognition of handwritten mathematical expressions with multi-task learning",
    author="",
    author_email="",
    # REPLACE WITH YOUR OWN GITHUB PROJECT LINK
    url="",
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    packages=find_packages(),
)
