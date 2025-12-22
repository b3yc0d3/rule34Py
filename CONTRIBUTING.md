# Contributing

Thanks for taking an interest in contributing to the rule34Py project!

* This project's **canonical upstream** is at https://github.com/b3yc0d3/rule34Py.
* File **bugs**, **enhancement requests**, and other **issues** to the GH issue tracker at https://github.com/b3yc0d3/rule34Py/issues.
* See the [Developer Guide](https://b3yc0d3.github.io/rule34Py/dev/developer-guide.html) for information about how to **build** this project from source and run tests.


## Submitting Changes

#. Base your development branch off of the [upstream](https://github.com/b3yc0d3/rule34Py/tree/develop) ``develop`` reference.

#. Before committing your changes, run the **project linter** using ``make``. It will use the ``ruff`` to lint all the project sources.

    .. code-block:: bash

        poetry install  # Optional, if you have not done it previously.
        make lint

    Fix or respond to any findings in the linter.

#. Run the project's test suite against your changes. Ensure that all tests pass.

    .. code-block:: bash

        poetry install  # Optional, if you have not done it previously.
        make check

#. Write a good commit message. If you are unsure of how, [this cbeams article](https://cbea.ms/git-commit/) gives reasonable suggestions. Commit your changes.

#. Fork the canonical upstream repository on github. \[[GitHub Docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)\]

#. Push your development branch to your own fork. [Open a new Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) against the upstream `develop` ref.

#. Submit your PR. Respond to any PR build failures or feedback from the maintainers.
