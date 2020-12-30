# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='rvid',
    version='0.1.0',
    description='A small package to replace values in dict on python',
    long_description=readme,
    author='Hiroki Asano',
    author_email='asano.hiroki@gmail.com',
    url='https://github.com/ashnoa/replace-value-in-python-dict',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

