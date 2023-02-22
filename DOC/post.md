## Class > Post
- [class Post](#post)
    - [from_json(\<json\>)](#from_json)
    - [id](#id)
    - [hash](#hash)
    - [score](#score)
    - [size](#size)
    - [image](#image)
    - [video](#video)
    - [thumbnail](#thumbnail)
    - [sample](#sample)
    - [content_type](#content_type)
    - [owner](#owner)
    - [tags](#tags)
    - [change](#change)
    - [directory](#directory)


### Post
Type: `class`\
Symtax: `post = Post(<id>, <hash>, <score>, <size>, <image>, <preview>, <sample>, <owner>, [<tags>], <file_type>, <directory>, <change>)`\
Args:\
&ensp;&ensp;&ensp;`id` __[int]__ Id of post\
&ensp;&ensp;&ensp;`hash` __[str]__ Post hash\
&ensp;&ensp;&ensp;`score` __[int]__ Score of post\
&ensp;&ensp;&ensp;`size` __[list(int, int)]__ Image size (eg. [HEIGHT, WIDTH])\
&ensp;&ensp;&ensp;`image` __[str]__ Url of image/video/gif\
&ensp;&ensp;&ensp;`preview` __[str]__ Url of thumbnail\
&ensp;&ensp;&ensp;`sample` __[str]__ Url of sample\
&ensp;&ensp;&ensp;`owner` __[str]__ Username of owner\
&ensp;&ensp;&ensp;`tags` __[list(str)]__ String list of tags
&ensp;&ensp;&ensp;`file_type` __[str]__ Content of post (e.g. gif, image or video)\
&ensp;&ensp;&ensp;`directory` __[int]__ Directory id of post\
&ensp;&ensp;&ensp;`change` __[int]__ Change timestamp of post\

Returns:\
&ensp;&ensp;&ensp; __[Post]__ Post Object

## from_json
Type: `function`\
Syntax: `<Post>.from_json(<json>)`\
Args:\
&ensp;&ensp;&ensp;`json` __[dict]__ Json post object from the rule34.xxx api.

Returns:\
&ensp;&ensp;&ensp;__[Post]__ [Post](https://github.com/b3yc0d3/rule34Py/blob/master/DOC/post.md#Post) object.

Create Post object directly from json.

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

### video
Type: `property`\
Syntax: `<Post>.video`\
Returns:\
&ensp;&ensp;&ensp; __[str]__ Url of video

Get post image

### thumbnail
Type: `property`\
Syntax: `<Post>.thumbnail`\
Returns:\
&ensp;&ensp;&ensp; __[str]__ Thumbnail image of post.

Get thumbnail image of post.

### sample
Type: `property`\
Syntax: `<Post>.sample`\
Returns:\
&ensp;&ensp;&ensp; __[str]__ Sample image of post.

Get sample image of post.

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

### content_type
Type: `property`\
Syntax: `<Post>.content_type`\
Returns:\
&ensp;&ensp;&ensp; __[str]__ Content type of post. (e. g. image, gif, video)

Get content type of post.

### change
Type: `property`\
Syntax: `<Post>.change`\
Returns:\
&ensp;&ensp;&ensp; __[int]__ Unix timestamp

Get change timestamp of post.

### directory
Type: `property`\
Syntax: `<Post>.directory`\
Returns:\
&ensp;&ensp;&ensp; __[int]__ Directory id

Get directory id of post.