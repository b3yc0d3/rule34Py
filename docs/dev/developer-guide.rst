===============
Developer Guide
===============


tl;dr
=====

.. code-block:: bash

    pip install . .[docs] .[dev] .[test]
    make all    # build wheel
    make check  # run unit tests
    make dist   # build sdist
    make html   # build documentation
    make lint   # run project linter


Project Layout
==============

* ``.github/`` contains GitHub specific workflows, actions, and templates.

* ``docs/`` contains project documentation, including the source for the sphinx-generated documentation.

* ``rule34Py/`` contains the source code for the ``rule34Py`` package.

* ``tests/`` contains the project test suite.

    * ``tests/unit/`` contains the project unit-tests, which can be run without building or installing the project.


Building the project from source
================================

This project can be built directly from source using a few host tools.
Supported development environments include:

- Ubuntu 24.04
- Windows

The following instructions are written on the assumption that you are building in a Linux environment.

#. Start by cloning the repository with ``git``.

    .. code-block:: bash

        git clone https://github.com/b3yc0d3/rule34Py.git
        cd rule34Py

#. (Optional. Recommended.) Setup a python virtual environment.

    .. code-block:: bash

        python -m venv .venv
        echo "/.venv" >>.git/info/exclude  # excludes your venv from git tracking
        source .venv/bin/activate

#. Install project python dependencies from the ``pyproject.toml`` file. Use ``GNU Make`` to build the project. The ``all`` make target (the default) builds the project's wheels.

    .. code-block:: bash

        pip install . .[dev]
        make all

    Build output will be placed in the ``:build/`` directory in your workspace.

Other ```make`` targets are supported to ``clean`` the project and build other artifacts.
Generally, the project ``Makefile`` honors the `GNU Standard Targets <https://www.gnu.org/software/make/manual/html_node/Standard-Targets.html>`_ specification.


Running the project test suite
==============================

#. Setup your build environment as in the "Building the project from source" section.

#. Install the optional test dependencies and invoke their ``make`` target.

    .. code-block:: bash

        pip install .[test]
        make test

For more information, reference the ``:tests/README.md`` file.


Building the project documentation
==================================

#. Setup your build environment as in the "Building the project from source" section.

#. Install the optional docs dependencies and invoke their ``make`` target.

    .. code-block:: bash

        pip install .[docs]
        make html

    Build output will be placed in the ``:build/html/`` directory.

#. (Optional.) Host the build output locally to test changes.

    .. code-block:: bash

        cd build/html
        python -m http.server 8080

    Python will host the docs site at http://localhost:8080.


Integrating this project
========================

This project is `licensed <./license.html#license>`_ under the GPLv3 license.
Ensure that your project's licensing strategy is compatible with the GPL.
For more information, reference the GNU reference guide for GPLv3 `here <https://www.gnu.org/licenses/gpl-3.0.en.html>`_.

All direct dependencies of this project are either GPL licensed, or are licensed more permissively.
But testing code does call the ``reponses`` module, which is licensed under the Apache 2.0 license.
Reference the `:NOTICE.md <./license.html#notice>`_ file for more information.
