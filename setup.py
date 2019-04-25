"""
Build a python package
"""
from setuptools import setup

setup(
    name="olc",
    # PEP-440 compatible version
    version="0.0.2",
    url="https://github.com/rommelag/olc",
    author="Rommelag iLabs",
    description=("Basic Open Source License Collector"),
    license="0BSD",
    packages=["olc"],
    install_requires=[],
    scripts=['detect_licenses']
)
