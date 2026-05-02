How to get package metadata
===========================

Rule34Py is generally a `PEP440 <https://peps.python.org/pep-0440/>`_-compliant package.
Therefore, it provides package metadata describing critical details relevant to package integrators.

This guide describes how to extract pieces of that package metadata, from your installed copy of rule34Py.


Ownership and Maintainership
----------------------------

Extract the package's **maintainership** information by interrogating the ``Maintainer*`` fields using the ``importlib.metadata`` module.

.. code-block:: python

	from importlib.metadata import metadata
	maintainer = metadata("rule34Py")["Maintainer"]
	maintainer_email = metadata("rule34Py")["Maintainer-email"]

The package's canonical **author** is the same as the maintainer.

If you need detailed information about who authored a specific segment of the project code, use ``git blame`` to interrogate the code files directly.


Project Version
---------------

Extract the project's **version** information using the ``importlib.metadata.version`` method.

.. code-block:: python

	from importlib.metadata import version
	rule34Py_version = version("rule34Py")

The project's version is guaranteed to be PEP440 compliant.

.. tip::

	You can also get the project version from the ``importlib.metadata.metadata("rule34Py")["Version"]`` field.


License Information
-------------------

Extract the project's SPDX license identifier by interrogating the package metadata ``License`` field.

.. code-block:: python

	from importlib.metadata import metadata
	license = metadata("rule34Py")["License"]

The direct :ref:`license text<license-text>` and :ref:`notice text<notice-text>` can be taken from the project documentation, or from the distribution ``:LICENSE`` and ``:NOTICE.md`` files respectively.
