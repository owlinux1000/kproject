# -*- coding: utf-8 -*-
from setuptools import setup, find_packages  

setup(
    name='kproject',
    version="1.0.10",
    description='Initializing tool for Machine Learning',
    author='Chihiro Hasegawa',
    author_email='pgm3rdlinuxor1000@gmail.com',
    license='MIT',
    packages=['kproject'],
    entry_points="""
    [console_scripts]
    kproject = kproject.kproject:main
    """,
)
