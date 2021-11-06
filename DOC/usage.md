# Usage
- [Class rule34Py](#rule34py)
    - [get_comments(\<post_id>)](#get_post)
    - [get_post(\<post_id>)](#get_post)
    - [icame()](#icame)
    - [random_post([?tags])](#random_post)
    - [search([tags], \<?page_id>, \<?limit>)](#search)
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
&ensp;&ensp;&ensp;__[list(PostComment)]__ List of [PostComment](./post_comment.md)

Get comments of given Post

## get_post
Type: `function`\
Syntax: `<rule34Py>.get_post(<post_id>)`\
Args:\
&ensp;&ensp;&ensp;`post_id` __[int]__ Id of post

Returns:\
&ensp;&ensp;&ensp;__[Post]__ Single [Post](./page.md)

Get Post by Id

## icame
Type: `function`\
Syntax: `<rule34Py>.icame()`\
Returns:\
&ensp;&ensp;&ensp;__[list(ICame)]__ List of [ICame](#./icame.md) Objects

## random_post
Type: `function`\
Syntax: `<rule34Py>.random_post([?tags])`\
Args:\
&ensp;&ensp;&ensp;`tags` __[list(str)]__ String list of tags (*Optional*)

Returns:\
&ensp;&ensp;&ensp; __[Post]__ Post Object

## search
Type: `function`\
Syntax: `<rule34Py>.search([tags], <?page_id>, <?limit>)`\
Args:\
&ensp;&ensp;&ensp;`tags` __[list(str)]__ String ist of tags\
&ensp;&ensp;&ensp;`page_id` __[int]__ Page id (*Optional*)\
&ensp;&ensp;&ensp;`limit` __[int(1-100)]__ Limit of posts returnt. Default is 100 (*Optional*)

Returns:\
&ensp;&ensp;&ensp;__[list(Post)]__ List of [Posts](./page.md)

Search for posts by tags. _Wilde card supported_ ([Cheatsheet](https://rule34.xxx/index.php?page=help&topic=cheatsheet) and [Tags](https://rule34.xxx/index.php?page=tags&s=list))

## version
Type: `proerty`\
Syntax: `<rule34Py>.version`\
Returns:\
&ensp;&ensp;&ensp; __[str]__ Version string
