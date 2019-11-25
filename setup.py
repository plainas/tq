#!/usr/bin/python3

from distutils.core import setup

setup(
    name='tq',
    version='0.2.1',
    description='Comand line css selector over HTML',
    author='Pedro',
    author_email='pedroghcode@gmail.com',
    url='https://github.com/plainas/tq',
    packages= ['tq'],
    scripts=['bin/tq'],
    install_requires=[
        'beautifulsoup4==4.8.1',
        'setuptools==39.0.1'
        ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)
