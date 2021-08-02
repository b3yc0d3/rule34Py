# rule34Py
[![Downloads](https://pepy.tech/badge/rule34py)](https://pepy.tech/project/rule34py) ![](https://img.shields.io/pypi/format/rule34Py) [![](https://img.shields.io/pypi/v/rule34Py)](https://pypi.org/project/rule34Py/) ![](https://img.shields.io/github/license/b3yc0d3/rule34Py) ![](https://img.shields.io/github/languages/code-size/b3yc0d3/rule34Py)\
This is a Simple rule34.xxx API wraper.

## Installation
`pip install rule34Py`
\
\
**Code Snippet:**
```python
from rule34Py import rule34Py

r34Py = rule34Py()

results = r34Py.search(['neko'], 5, 10)
favs = r34Py.getFavorites(118538, true)
comments = r34Py.getComments(4485507)
post = r34Py.getPost(4485507)
icameList = r34Py.iCameList()
random_0 = r34Py.random() # Complete Random
random_1 = r34Py.random(['neko', 'creampie']) # complete Random but tags oriented


print(results)
print(favs)
print(comments)
print(post)
print(icameList)
print(random_0)
print(random_1)
```

---

## Usage
- [Class: rule34Py](#rule34Py)
    - [getComments(<post_id>)](#getcomments)
    - [getFavorites(<user_id>, <?id_only>)](#getfavorites)
    - [getPost(<post_id>)](#getpost)
    - [search([\<tags>], <?page_id>, <?limit>)](#search)
    - [iCameList()](#icamelist)
    - [rabdom([\<?tags>])](#random)

## rule34Py
Syntax: `r34Py = rule34Py()`

Creates a new rule34Py instance.

## getComments
Syntax: `<rule34Py>.getCommanets(<post_id>)`
- `post_id` \<int>
- returns: \<list>[\<dictionary>]
    - `dictionary`> `{"id": <INT>, "creator_id": <INT>, "created_at": <STR>, "creator": {"name": <STR>, "id": <INT>}, "content": <STR>}`

Get Comments from a Post.

## getFavorites
Syntax: `<rule34Py>.getFavorites(<user_id>, <?id_only>)`
- `user_id` \<int>
- `id_only` \<boolean> (Optional, Defaults is false)
- returns: \<list>[\<dictionary>]
    - `dictionary`> `{"id": <INT>, "score": <INT>, "rating": <STR>, "creator_id": <INT>, "created_at": <STR>, "source": <STR>, "has_notes": <BOOL>, "tags": <LIST>[<STR>], "img_sample_url": <STR>, "img_file_url": <STR>, "img_preview_url": <STR>, "has_children": <BOOL>, "parent_id": <INT>, "has_comments": <BOOL>}`

Gets Favorites from a User.

## getPost
Syntax: `<rule34Py>.getPost(<post_id>)`
- `post_id` \<int>
- returns: \<dictionary>
    - `dictionary`> `{"id": <INT>, "score": <INT>, "rating": <STR>, "creator_id": <INT>, "created_at": <STR>, "source": <STR>, "has_notes": <BOOL>, "tags": <LIST>[<STR>], "img_sample_url": <STR>, "img_file_url": <STR>, "img_preview_url": <STR>, "has_children": <BOOL>, "parent_id": <INT>, "has_comments": <BOOL>}`

Gets Post by ID.

## search
Syntax: `<rule34Py>.search([<tags>], <?page_id>, <?limit>)`
- `tags` \<list> ([Tag Cheatsheet](https://rule34.xxx/index.php?page=tags&s=list))
- `page_id` \<int>
- `limit` \<int> (Optional, Defaults is 100 and max limit is 100)
- returns: \<list>[\<int>, ..\<dictionary>]
    - `"<POST_COUNT>"` \<int> [*only first item of list*]
    - `dictionary`> `{"id": <INT>, "score": <INT>, "rating": <STR>, "creator_id": <INT>, "created_at": <STR>, "source": <STR>, "has_notes": <BOOL>, "tags": <LIST>, "img_sample_url": <STR>, "img_file_url": <STR>, "img_preview_url": <STR>}`

## iCameList
Syntax: `<rule34Py>.iCameList()`
- returns: \<list>[\<dictionary>]
    - `dictionary`> `{"tag": <STR>, "icame_count": <INT>, "tag_url": <STR>}`


## random
Syntax: `<rule34Py>.random([<?tags>])`
- `tags` \<list> ([Tag Cheatsheet](https://rule34.xxx/index.php?page=tags&s=list))
- returns: \<dict>
    - `dictionary`> `{"id": <INT>, "score": <INT>, "rating": <STR>, "creator_id": <INT>, "created_at": <STR>, "source": <STR>, "has_notes": <BOOL>, "tags": <LIST>[<STR>], "img_sample_url": <STR>, "img_file_url": <STR>, "img_preview_url": <STR>, "has_children": <BOOL>, "parent_id": <INT>, "has_comments": <BOOL>}`
