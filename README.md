# rule34Py
![](https://img.shields.io/github/license/NikiNikOfficially/rule34Py) ![](https://img.shields.io/github/languages/code-size/NikiNikOfficially/rule34Py)\
This is a Simple rule34.xxx API wraper.

## Installation
`pip install rule34Py`
\
\
**Code Snippet:**
```python
from rule34Py import rule34Py

r34Py = rule34Py()

favs = r34Py.getFavorites(118538, true)

print(favs)
```

---

## Usage
- [Class: rule34Py](#rule34Py)
    - [getCommanets(<post_id>)](#getcommanets)
    - [getFavorites(<user_id>, <?id_only>)](#getfavorites)
    - [getPost(<post_id>)](#getpost)
    - [search(<tags>, <?limit>)](#search)

## rule34Py
Syntax: `r34Py = rule34Py()`

Creates a new rule34Py instance.

## getCommanets
Syntax: `<rule34Py>.getCommanets(<post_id>)`
- `post_id` \<int>
- returns: \<list>

Get Comments from a Post.

## getFavorites
Syntax: `<rule34Py>.getFavorites(<user_id>, <?id_only>)`
- `user_id` \<int>
- `id_only` \<boolean> (Optional, Defaults is false)
- returns: \<list>

Gets Favorites from a User.

## getPost
Syntax: `<rule34Py>.getPost(<post_id>)`
- `post_id` \<int>
- returns: \<dictionary>

Gets Post by ID.

## search
Syntax: `<rule34Py>.search(<tags>, <?limit>)`
- `tags` \<str_list>
- `limit` \<int> (Optional, Defaults is 100 and max limit is 100)
- returns: \<dictionary>

Searches for Posts by Tag\
[Tag Cheatsheet](https://rule34.xxx/index.php?page=tags&s=list)
