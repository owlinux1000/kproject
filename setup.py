# -*- coding: utf-8 -*-
from __init__ import *
from setuptools import setup, find_packages  

setup(
    name=name,
    version=version,
    description=description,
    author=author,
    author_email=author_email,
    license=license,
    packages=find_packages(),
    entry_points="""
    [console_scripts]
    kproject = kproject.kproject:main
    """,
)
