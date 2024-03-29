#!/usr/bin/env python

"""The setup script."""

from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = [
]

extra_requires_dev = [
    'pytest',
    'pytest-cov',
    'moto',
    'tox',
    'flake8',
]

setup(
    name='package1',
    description="test package",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Althaf",
    author_email='althafnawadir2003@gmail.com}',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6',
    install_requires=install_requires,
    extras_require={'dev': extra_requires_dev},
    include_package_data=True
)
