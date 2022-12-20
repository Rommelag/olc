"""
Build a python package
"""
from os import path
from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="olc",
    # PEP-440 compatible version
    version="0.0.4",
    url="https://github.com/rommelag/olc",
    author="Rommelag iLabs",
    description=("Basic Open Source License Collector"),
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="0BSD",
    packages=["olc"],
    install_requires=[],
    scripts=['detect_licenses']
)
