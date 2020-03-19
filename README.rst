=================
flake8-no-fstring
=================

.. image:: https://img.shields.io/pypi/v/flake8-no-fstring.svg
        :target: https://pypi.python.org/pypi/flake8-no-fstring

.. image:: https://img.shields.io/travis/adamchainz/flake8-no-fstring.svg
        :target: https://travis-ci.org/adamchainz/flake8-no-fstring

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/python/black

A `flake8 <https://flake8.readthedocs.io/en/latest/index.html>`_ plugin to ban
f-string.

This can be useful in code bases where packages are shared between two different
python versions, one of which does not support f-strings.

Installation
------------

Install from ``pip`` with:

.. code-block:: sh

     python -m pip install flake8-no-fstring

Python 3.6 to 3.8 supported.

When installed it will automatically be run as part of ``flake8``; you can
check it is being picked up with:

.. code-block:: sh

    $ flake8 --version
    3.7.9 (flake8-no-fstring: 1.0.0, mccabe: 0.6.1, pycodestyle: 2.5.0, pyflakes: 2.1.1) CPython 3.8.0 on Darwin

Rules
-----

NF001: No f-string
~~~~~~~~~~~~~~~~~~

Complains about f-strings.
