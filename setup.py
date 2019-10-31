#!/usr/bin/python3

from distutils.core import setup

from tq import VERSION

setup(
    name='tq',
    version=VERSION,
    description='Comand line css selector over HTML',
    author='Pedro',
    author_email='pedroghcode@gmail.com',
    url='https://github.com/plainas/tq',
    packages= ['tq'],
    scripts=['bin/tq'],
    install_requires=['beautifulsoup4>=4.8.1'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)
