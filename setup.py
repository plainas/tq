#!/usr/bin/python3

from distutils.core import setup

setup(
    name='tq',
    version='0.2.0',
    description='comand line css selector',
    author='Pedro',
    author_email='pedro@example.com',
    url='https://github.com/plainas/tq',
    packages= ['tq'],
    scripts=['bin/tq'],
    install_requires=["beautifulsoup4==4.4.0"]
)