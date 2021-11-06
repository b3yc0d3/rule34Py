## Class > PostComment
- [class PostComment](#postcomment)
    - [id](#id)
    - [author_id](#author_id)
    - [body](#body)
    - [post_id](#post_id)
    - [creation](#creation)

### PostComment
Type: `class`\
Syntax: `pContent = PostComment(<id>, <owner_id>, <body>, <post_id>, <creation>)`\
Args:\
&ensp;&ensp;&ensp;`id` __[int]__ Id of comment\
&ensp;&ensp;&ensp;`owner_id` __[int]__ Id of comment author\
&ensp;&ensp;&ensp;`body` __[str(UTF-8)]__ Body of Comment\
&ensp;&ensp;&ensp;`post_id` __[int]___ Id of parent post\
&ensp;&ensp;&ensp;`creation` __[str]__ Creation timestamp

Returns:\
&ensp;&ensp;&ensp;__[PostComment]__ Post

### id
Type: `property`\
Syntax: `<PostComment>.id`\
Returns:\
&ensp;&ensp;&ensp;__[int]__ Id of comment

Id of comment

### author_id
Type: `property`\
Syntax: `<PostComment>.author_id`\
Returns:\
&ensp;&ensp;&ensp;__[int]__ Id of author

Id of comment author

### body
Type: `property`\
Syntax: `<PostComment>.body`\
Returns:\
&ensp;&ensp;&ensp;__[str]__ Body of comment

Comment body

### post_id
Type: `property`\
Syntax: `<PostComment>.post_id`\
Returns:\
&ensp;&ensp;&ensp;__[int]__ Id of parent post

Id of parent post

### creation
Type: `property`\
Syntax: `<PostComment>.creation`\
Returns:\
&ensp;&ensp;&ensp;__[str]__ Creation Timestamp

Timestamp of creation
