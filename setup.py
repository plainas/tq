#!/usr/bin/python3

from distutils.core import setup

from build_manpage import BuildManPage

setup(
    name='tq',
    version='0.1',
    description='comand line css selector',
    author='Pedro',
    author_email='pedro@example.com',
    url='https://github.com/plainas/tq',
    packages= ['tq'],
    scripts=['bin/tq'],
    cmdclass={
        'build_manpage': BuildManPage,
    },
    install_requires=["beautifulsoup4=4.4.0"]
)