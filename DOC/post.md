## Class > Post
- [class Post](#post)
    - [id](#id)
    - [hash](#hash)
    - [score](#score)
    - [size](#size)
    - [image](#image)
    - [owner](#owner)
    - [tags](#tags)


### Post
Type: `class`\
Symtax: `post = Post(<id>, <hash>, <score>, <size>, <image>, <owner>, [<tags>])`\
Args:\
&ensp;&ensp;&ensp;`id` __[int]__ Id of post\
&ensp;&ensp;&ensp;`hash` __[str]__ Post hash\
&ensp;&ensp;&ensp;`score` __[int]__ Score of post\
&ensp;&ensp;&ensp;`size` __[list(int, int)]__ Image size (eg. [HEIGHT, WIDTH])\
&ensp;&ensp;&ensp;`image` __[str]__ Url of image\
&ensp;&ensp;&ensp;`owner` __[str]__ Username of owner\
&ensp;&ensp;&ensp;`tags` __[list(str)]__ String list of tags

Returns:\
&ensp;&ensp;&ensp; __[Post]__ Post Object

### id
Type: `property`\
Syntax: `<Post>.id`\
Returns:\
&ensp;&ensp;&ensp; __[int]__ Id of post

Get id of post

### hash
Type: `property`\
Syntax: `<Post>.hash`\
Returns:\
&ensp;&ensp;&ensp; __[str]__ Hash of post

Get hash of post

### score
Type: `property`\
Syntax: `<Post>.score`\
Returns:\
&ensp;&ensp;&ensp; __[int]__ Score of post

Get score of post

### size
Type: `property`\
Syntax: `<Post>.size`\
Returns:\
&ensp;&ensp;&ensp; __[list(int, int)]__ Image size of post (eg. [HEIGHT, WIDTH])

Get image size

### image
Type: `property`\
Syntax: `<Post>.image`\
Returns:\
&ensp;&ensp;&ensp; __[str]__ Url of image

Get post image

### owner
Type: `property`\
Syntax: `<Post>.owner`\
Returns:\
&ensp;&ensp;&ensp; __[str]__ Username

Get username of post creator

### tags
Type: `property`\
Syntax: `<Post>.tags`\
Returns:\
&ensp;&ensp;&ensp; __[list(str)]__ String list of tags

Get tags of post
