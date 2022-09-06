#!/usr/bin/env python3

from setuptools import setup

setup(name='dev_aberto_cesarea',
      version='0.1',
      packages=['dev_aberto'],
      install_requires=[
        'pacote>=1.0',
        'pacote2'
    ],
    scripts=['scripts/hello.py'],
      )