<div align="center">

# rule34py

![GPL-3.0](https://img.shields.io/github/license/b3yc0d3/rule34Py) [![](https://img.shields.io/pypi/v/rule34Py)](https://pypi.org/project/rule34Py/) [![](https://img.shields.io/pypi/dm/rule34py?color=blue)](https://pypi.org/project/rule34Py/)

Python API wrapper for [rule34.xxx](https://rule34.xxx/).
</div>


## Installation

[rule34Py](https://pypi.org/project/rule34Py/) is available directly from the Python Package Index and can be installed via `pip`.

```bash
pip install rule34Py
```

Or you can build it from source using this project.
See the [Developer Guide](https://b3yc0d3.github.io/rule34Py/dev/developer-guide.html) for more information.


## Quickstart

```python
from rule34Py import rule34Py
r34Py = rule34Py()

# Get comments of an post.
r34Py.get_comments(4153825)

# Get post by its id.
r34Py.get_post(4153825)

# Get top 100 icame.
r34Py.icame()

# Search for posts by tag(s).
r34Py.search(["neko"], page_id=2, limit=50)

# Get pool by id.
r34Py.get_pool(28)

# Get a random post.
random = r34Py.random_post()

# Get just a random post ID.
random_id = r34Py.random_post_id()
```


## Documentation

This project has extensive [documentation]((https://b3yc0d3.github.io/rule34Py/), hosted on the upstream Github Pages.

The documentation includes additional **Tutorials**, **User Guides**, **API Documentation**, and more.


### Committing your Changes
- Before committing your changes, run the project **linter** by calling `make lint`.
- Branch name should be prefixed with
    - `fix-` when fixing an bug/error
    - `feat-` when a feature got added
    - `chore-` everything else that doesn't fall in the above categories
- The title must describe what your pull request changes/does.
- Write a brief description of what the pull request does/solves in the commit.
- If your pull request fixes an issue, please mention that issue in the commit title.

Example structure of a commit message
```
here goes the title of the commit

Here goes the description
```

The title shall not be longer then 50 characters.
**Select the `develop` branch for pull requests.**
