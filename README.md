## rule34Py [![Downloads](https://pepy.tech/badge/rule34py)](https://pepy.tech/project/rule34py) ![](https://img.shields.io/pypi/format/rule34Py) [![](https://img.shields.io/pypi/v/rule34Py)](https://pypi.org/project/rule34Py/) ![](https://img.shields.io/github/license/b3yc0d3/rule34Py) ![](https://img.shields.io/github/languages/code-size/b3yc0d3/rule34Py)
This is a Simple rule34.xxx API wraper.<br>
Read the [Documentation](#documentation)


## Whats new?
See [Changelog](https://github.com/b3yc0d3/rule34Py/blob/master/CHANGELOG.md) for more informations.


## Documentation
New [Documentation](https://github.com/b3yc0d3/rule34Py/blob/master/DOC/usage.md) for current version<br>
Old [Documentation](https://github.com/b3yc0d3/rule34Py/blob/master/DOC/old.md) (*for version <u>1.3.38</u> and below!*)


## Ideas
Moved to [TODO.md](https://github.com/b3yc0d3/rule34Py/blob/master/TODO.md) or/and see Issues.


## Installation
`pip install rule34Py`


## Code Snippet
```py
from rule34Py import rule34Py

r34Py = rule34Py()

print(r34Py.version)

result_comments = r34Py.get_comments(4153825)
result_post = r34Py.get_post(4931536)
result_icame = r34Py.icame()
result_search = r34Py.search(["neko"], page_id=2, limit=50)
result_pool = r34Py.get_pool(17509) # or r34Py.get_pool(17509, false)
result_random = r34Py.random_post(["neko"]) # or r34Py.random_post()
result_tagmap = r34Py.tagmap()

# Stats
result_topTaggers = r34Py.stats.top_taggers()
result_topCommenters = r34Py.stats.top_commenters()
result_topForumPosters = r34Py.stats.top_forum_posters()
result_topImagePosters = r34Py.stats.top_image_posters()
result_topNoteEditors = r34Py.stats.top_note_editors()
result_topFavorites = r34Py.stats.top_favorites()

print(result_random.id)
print(result_random.image)

print(result_icame[0].character_name) # returns the character name of the first item

print(result_tagmap[0].tagname)
```

## Build it your self
```console
foo@bar:~$ git clone git@github.com:b3yc0d3/rule34Py.git
foo@bar:~$ cd rule34Py

(on linux just run; ./build.sh)
foo@bar:~$ python setup.py bdist_wheel
foo@bar:~$ python setup.py sdist
foo@bar:~$ python setup.py bdist_wheel sdist

foo@bar:~$ pip install -e .
```