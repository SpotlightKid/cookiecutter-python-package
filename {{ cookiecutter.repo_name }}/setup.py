#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


exec(open('{{ cookiecutter.package_name }}/version.py').read())

classifiers = """
# The next line is important: it prevents accidental upload to PyPI!
Private :: Do Not Upload
Development Status :: 2 - Pre-Alpha
Intended Audience :: Developers
License :: Other/Proprietary License
#Operating System :: Microsoft :: Windows
Operating System :: POSIX
#Operating System :: MacOS :: MacOS X
Programming Language :: Python
Programming Language :: Python :: 2.7
#Programming Language :: Python :: 3.4
Topic :: Internet
"""

install_requires = [
    # 'six',
]


setup(
    name='{{ cookiecutter.project_name }}',
    version=__version__,  # noqa
    description='{{ cookiecutter.project_description }}',
    long_description=open('README.rst').read(),
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    url='{{ cookiecutter.project_url }}',
    license="{{ cookiecutter.license }}",
    classifiers=[c.strip() for c in classifiers.splitlines()
                 if c.strip() and not c.startswith('#')],
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    test_suite='tests',
    install_requires=install_requires,
)
