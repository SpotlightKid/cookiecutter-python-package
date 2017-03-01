Python Package Cookiecutter Template
------------------------------------

You want to start a new Python project? Then please use this project template.

Install cookiecutter from PyPI (do not install it via your system package
manager, because the version you'll get will probably be too old). You need
at least cookiecutter version 1.4.0:

    $ [sudo] pip install -U [--user] cookiecutter

Create the project structure:

    $ cookiecutter https://github.com/SpotlightKid/python-package-cookiecutter.git

Customize:

1. Adapt LICENSE.rst
2. Adapt setup.py (license, classifiers, install_requires)
3. Write tests
4. Write app
5. Run tests
6. Edit README.rst and adapt quickstart instructions
7. Release!


Have fun!


TODO
----

* Add pydocstyle configuration
* Add pylint configuration
* Check parameter definition in docstrings?
