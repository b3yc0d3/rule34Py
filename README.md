<div align="center">

# rule34py

![GPL-3.0](https://img.shields.io/github/license/b3yc0d3/rule34Py) [![](https://img.shields.io/pypi/v/rule34Py)](https://pypi.org/project/rule34Py/) [![](https://img.shields.io/pypi/dm/rule34py?color=blue)](https://pypi.org/project/rule34Py/)

Python api wrapper for [rule34.xxx](https://rule34.xxx/).
</div>

## Getting Started

#### Install it using pip
```
pip install rule34py
```

#### Install it from Source
```
git clone https://github.com/b3yc0d3/rule34Py.git
cd rule34Py
python setup.py sdist
pip install -e .
```

## Documentation
You can find the documentation [here](https://github.com/b3yc0d3/rule34Py/tree/master/DOC).

> [!NOTE]
> The documentation might move in the future.

## Code Snippet
```py
from rule34Py import rule34Py
r34Py = rule34Py()

# get comments of an post
r34Py.get_comments(4153825)

# get post by its id
r34Py.get_post(4153825)

# get top 100 icame
r34Py.icame()

# search for posts by tag(s)
r34Py.search(["neko"], page_id=2, limit=50)

# get pool by id
r34Py.get_pool(17509)

# get a random post (in this case with tag(s))
random = r34Py.random_post(["neko"])

# get general site stats
r34Py.stats.top_taggers()
r34Py.stats.top_commenters()
r34Py.stats.top_forum_posters()
r34Py.stats.top_image_posters()
r34Py.stats.top_note_editors()
r34Py.stats.top_favorites()
```
