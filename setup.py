#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages
import re


def find_version():
    return re.search(r"^__version__ = '(.*)'$",
                     open('irwin/version.py', 'r').read(),
                     re.MULTILINE).group(1)


setup(name='irwin',
      version=find_version(),
      description=' Plotting data in the terminal.',
      long_description=open('README.rst', 'r').read(),
      author='Erik Moqvist',
      author_email='erik.moqvist@gmail.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
      ],
      keywords=[],
      url='https://github.com/eerimoq/irwin',
      packages=find_packages(exclude=['tests']),
      install_requires=[],
      test_suite="tests",
      include_package_data=True)
