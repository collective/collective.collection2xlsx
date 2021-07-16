.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

.. image:: https://github.com/collective/collective.collection2xlsx/actions/workflows/plone-package.yml/badge.svg
    :target: https://github.com/collective/collective.collection2xlsx/actions/workflows/plone-package.yml

.. image:: https://codecov.io/gh/collective/collective.collection2xlsx/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/collective/collective.collection2xlsx

.. image:: https://codecov.io/gh/collective/collective.collection2xlsx/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/collective/collective.collection2xlsx

.. image:: https://img.shields.io/pypi/v/collective.collection2xlsx.svg
    :target: https://pypi.python.org/pypi/collective.collection2xlsx/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/collective.collection2xlsx.svg
    :target: https://pypi.python.org/pypi/collective.collection2xlsx
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/collective.collection2xlsx.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/collective.collection2xlsx.svg
    :target: https://pypi.python.org/pypi/collective.collection2xlsx/
    :alt: License


==========================
collective.collection2xlsx
==========================

The add-on allows you to export the tabular view of a Collection as an Excel (XLSX) file.

Features
--------

- Export Collection items in XLSX format


Translations
------------

This product has been translated into

- english
- german


Installation
------------

Install collective.collection2xlsx by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.collection2xlsx


and then running ``bin/buildout``

Usage
-----

You can call the ``xlsx`` view on every Collection, but it makes more sence when you choose what columns to show for the tabular view.
The add-on will add a xlsx-action for Collections, so that users can just click the link to download the list as XLSX file.


Authors
-------

This add-on was build by `Derico <https://derico.de>`_ [MrTango].


Contributors
------------

Put your name here, you deserve it!

- ?


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.collection2xlsx/issues
- Source Code: https://github.com/collective/collective.collection2xlsx



Support
-------

If you are having issues, please let us know.



License
-------

The project is licensed under the GPLv2.
