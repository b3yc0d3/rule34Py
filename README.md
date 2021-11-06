# rule34Py
[![Downloads](https://pepy.tech/badge/rule34py)](https://pepy.tech/project/rule34py) ![](https://img.shields.io/pypi/format/rule34Py) [![](https://img.shields.io/pypi/v/rule34Py)](https://pypi.org/project/rule34Py/) ![](https://img.shields.io/github/license/b3yc0d3/rule34Py) ![](https://img.shields.io/github/languages/code-size/b3yc0d3/rule34Py)\
This is a Simple rule34.xxx API wraper.\
You can finde the Changelog [_here_](./change_log.txt).

## Ideas
+ [ ] User search

*Feel free to submit ideas*


## Installation
`pip install rule34Py`

## Documentation
New [Documentation](./DOC/usage.md) for current version\
Old [Documentation](./DOC/old.md) (*for version <u>1.3.38</u> and below!*)

## Code Snipped
```py
from rule34Py import rule34Py

r34Py = rule34Py()

result_comments = r34Py.get_comments(4153825)
result_post = r34Py.get_post(4931536)
result_icame = r34Py.icame()
result_search = r34Py.search(['neko'], page_id=2, limit=50)
result_random = r34Py.random("neko") # or r34Py.random()

print(result_random.id)
print(result_random.image)

print(result_icame[0].character_name) # returns the character name of the first item
```
