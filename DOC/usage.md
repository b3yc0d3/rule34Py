# Usage
- [Class rule34Py](#rule34py)
    - [get_comments(\<post_id>)](#get_post)
    - [get_pool(\<pool_id>, \<?fast>)](#get_pool)
    - [get_post(\<post_id>)](#get_post)
    - [icame()](#icame)
    - [random_post([?tags])](#random_post)
    - [search([tags], \<?page_id>, \<?limit>)](#search)
    - [tagmap()](#tagmap)
    - [version](#version)

## rule34Py
Type: `class`\
Syntax: `r34Py = rule34Py()`\
Creates a new rule34Py instance.

## get_comments
Type: `function`\
Syntax: `<rule34Py>.get_comments(<post_id>)`\
Args:\
&ensp;&ensp;&ensp;`post_id` __[int]__ Id of post

Returns:\
&ensp;&ensp;&ensp;__[list(PostComment)]__ List of [PostComment](https://github.com/b3yc0d3/rule34Py/blob/master/DOC/post_comment.md)

Get comments of given Post

## get_pool
Type: `function`\
Syntax: `<rule34Py>.get_pool(<pool_id>, <?fast>)`\
Args:\
&ensp;&ensp;&ensp;`pool_id` __[int]__ Id of pool\
&ensp;&ensp;&ensp;`fast` __[bool]__ If false returns [Post](https://github.com/b3yc0d3/rule34Py/blob/master/DOC/post.md) list, if true returns Id list (*Optional*)

Returns:\
&ensp;&ensp;&ensp;__[list(Post|str)]__ List of [Post](https://github.com/b3yc0d3/rule34Py/blob/master/DOC/post.md) Objects or List of Id string

Get Pool by Id
*Be aware that if "fast" is set to False, it takes extreme long.*

## get_post
Type: `function`\
Syntax: `<rule34Py>.get_post(<post_id>)`\
Args:\
&ensp;&ensp;&ensp;`post_id` __[int]__ Id of post

Returns:\
&ensp;&ensp;&ensp;__[Post]__ Single [Post](https://github.com/b3yc0d3/rule34Py/blob/master/DOC/post.md)

Get Post by Id

## icame
Type: `function`\
Syntax: `<rule34Py>.icame()`\
Returns:\
&ensp;&ensp;&ensp;__[list(ICame)]__ List of [ICame](https://github.com/b3yc0d3/rule34Py/blob/master/DOC/icame.md) Objects

Gets a list of the top 100 "came-on characters"

## random_post
Type: `function`\
Syntax: `<rule34Py>.random_post([?tags])`\
Args:\
&ensp;&ensp;&ensp;`tags` __[list(str)]__ String list of tags (*Optional*)

Returns:\
&ensp;&ensp;&ensp; __[Post]__ Post Object

Get a random Post

## search
Type: `function`\
Syntax: `<rule34Py>.search([tags], <?page_id>, <?limit>)`\
Args:\
&ensp;&ensp;&ensp;`tags` __[list(str)]__ String ist of tags\
&ensp;&ensp;&ensp;`page_id` __[int]__ Page id (*Optional*)\
&ensp;&ensp;&ensp;`limit` __[int(1-100)]__ Limit of posts returnt. Default is 100 (*Optional*)

Returns:\
&ensp;&ensp;&ensp;__[list(Post)]__ List of [Posts](https://github.com/b3yc0d3/rule34Py/blob/master/DOC/post.md)

Search for posts by tags. _Wilde card supported_ ([Cheatsheet](https://rule34.xxx/index.php?page=help&topic=cheatsheet) and [Tags](https://rule34.xxx/index.php?page=tags&s=list))

## tagmap
Type: `function`\
Syntax: `<rule34Py>.tagmap()`\
Returns:\
&ensp;&ensp;&ensp; __[list(dict)]__ List of dicts (eg. : `[{"rank": <int>, "tagname": <str>, "percentage": <float>}]`)

Get TagMap (Top 100 Tags searched)

## version
Type: `proerty`\
Syntax: `<rule34Py>.version`\
Returns:\
&ensp;&ensp;&ensp; __[str]__ Version string

Get current version of module (*eg. 1.4.1*)
