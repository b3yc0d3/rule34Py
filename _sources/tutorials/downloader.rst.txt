===============================
A Simple Rule34 Post Downloader
===============================

This tutorial walks you through creating a simple script that searches for and downloads a selection of posts from the `rule34.xxx <https://rule34.xxx/>`_ website using the rule34Py module.


1. Install python dependencies from PyPI, using PIP (or your python package manager of choice).

.. code-block:: bash

    python -m pip install rule34Py
    python -m pip install requests

2. Import the ``rule34Py`` module and instantiate a ``rule34Py`` client object.

The client brokers interactions with the public Rule34.xxx API endpoints.
It will transparently use the correct endpoint for whatever operation you request.
Data returned by the API will be marshalled into native python data types.


.. literalinclude:: downloader.py
    :language: python
    :lineno-start: 1
    :lines: 1-3

3. Use the ``rule34Py.search()`` method to search your tags.

The ``search()`` method accepts a list of tags.
You can use the same tag syntaxes that are supported on the interactive site's `Searching Cheatsheet <https://rule34.xxx/index.php?page=help&topic=cheatsheet>`_.

.. literalinclude:: downloader.py
    :language: python
    :lineno-start: 5
    :lines: 5-7

.. important::

    In this example, we are excluding posts tagged "video", so that we do not have to handle them specially during the download step.

.. note::

    By default, the ``search()`` method will return the first 1000 search results.
    You can change this behavior by setting the ``limit`` method parameter. For this example, we will only download the first 3 results, and ignore the remainder.

4. Download the images and save them to your local disk.

.. literalinclude:: downloader.py
    :language: python
    :lineno-start: 9
    :lines: 9-


--------------
Example Script
--------------

The complete, example script might look like this.

.. literalinclude:: downloader.py
    :language: python
    :linenos:
    :name: downloader_py
