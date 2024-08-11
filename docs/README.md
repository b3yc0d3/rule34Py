# Rule34Py Documentation

Last edited at `25-12-2023` by [b3yc0d3](https://github.com/b3yc0d3)

Parameters that are prefixed by an `?` are optional.

## rule34Py
rule34.xxx API wrapper.

### Functions
<details>
<summary><code>__init__() </code> - rule34.xxx API wrapper</summary>

rule34.xxx API wrapper.

</details>

<details>

<summary><code>get_comments(post_id: int) -> list[PostComment]</code> - Retrieve comments of post by its id</summary>

Retrieve comments of post by its id.

##### Parameters
| Parameter | Type  | Description |
|:----------|:------|:------------|
| `post_id` | `int` | Posts id.   |

##### Returns
**`list[PostComment]`** - List of [PostComment](#postcomment)s.
</details>

<details>
<summary><code>get_pool(pool_id: int, ?fast: bool) -> list[Post|int]</code> - Retrieve pool by its id</summary>

Retrieve pool by its id.

**Be aware that if "fast" is set to False, it may takes longer.**

##### Parameters
| Parameter | Type   | Description                                                                              |
|:----------|:-------|:-----------------------------------------------------------------------------------------|
| `pool_id` | `int`  | Pools id.                                                                                |
| `fast`    | `bool` | Fast "mode", if set to true only a list of post ids will be returned. (default *false*). |

##### Returns
**`list[Post|int]`** - List of [post](#post) objects or post ids if `fast` is set to true.
</details>

<details>
<summary><code>get_post(post_id: int) -> Post</code> - Get post by its id</summary>

Get post by its id.

##### Parameters
| Parameter | Type  | Description |
|:----------|:------|:------------|
| `post_id` | `int` | Id of post. |

##### Returns
**`Post`** - [Post](#post) object.
</details>

<details>
<summary><code>icame(limit: int) -> list[ICame]</code> - Retrieve list of top 100 iCame list</summary>

Retrieve list of top 100 iCame list.

##### Parameters
| Parameter | Type  | Description                              |
|:----------|:------|:-----------------------------------------|
| `limit`   | `int` | Limit of returned items. (default `100`) |

##### Returns
**`list[ICame]`** - List of [iCame](#icame) objects.
</details>

<details>
<summary><code>random_post(?tags: list) -> Post</code> - Get a random post</summary>

Get a random post.

##### Parameters
| Parameter | Type        | Description                                                           |
|:----------|:------------|:----------------------------------------------------------------------|
| `tags`    | `list[str]` | Tag list to search. If none, post will be used regardless of it tags. |

##### Returns
**`Post`** - [Post](#post) object.
</details>

<details>
<summary><code>search(self, tags: list, ?page_id: int, ?limit: int, ?deleted: bool, ?ignore_max_limit: bool) -> list[Post]</code> - Search for posts</summary>

Search for posts

##### Parameters
| Parameter          | Type        | Description                                                    |
|:-------------------|:------------|:---------------------------------------------------------------|
| `tags`             | `list[str]` | List of tags.                                                  |
| `page_id`          | `int`       | Page number.                                                   |
| `limit`            | `init`      | Limit for posts returned per page (max. 1000).                 |
| `ignore_max_limit` | `bool`      | If limit of 1000 should be ignored. *Not intended to be used.* |

##### Returns
**`list[Post]`** - List of [Post](#post) objects for matching posts.
</details>

<details>
<summary><code>tagmap() -> list[TopTag]</code> - Retrieve list of top 100 global tags</summary>

Retrieve list of top 100 global tags.

##### Returns
**`list[TopTag]`** - List of global top 100 tags. See [TopTag](#toptag).
</details>

<details>
<summary><code>version -> str</code> - Rule34Py version</summary>

Rule34Py version.

##### Returns
**`str`** - Version of rule34py.
</details>

## Post

### Functions

<details>
<summary><code>__init__(id: int, hash: str, score: int, size: list[int, int], image: str, preview: str, sample: str, owner: str, tags: list[str], file_type: str, directory: int, change: int)</code> - Post Class</summary>

Post Class

##### Parameters
| Parameter   | Type             |
|:------------|:-----------------|
| `id`        | `int`            |
| `hash`      | `str`            |
| `score`     | `int`            |
| `size`      | `list[int, int]` |
| `image`     | `str`            |
| `preview`   | `str`            |
| `sample`    | `str`            |
| `owner`     | `str`            |
| `tags`      | `list[str]`      |
| `file_type` | `str`            |
| `directory` | `int`            |
| `change`    | `int`            |

</details>

<details>
<summary><code>from_json(json: str) -> Post</code> - Create Post from json data</summary>

Create Post from json data.

##### Parameters
| Parameter | Type  | Description                         |
|:----------|:------|:------------------------------------|
| `json`    | `str` | Json data from rule34.xxx REST Api. |

##### Returns
**`Post`** - Post object.
</details>

### Properties
<details>
<summary><code>change() -> int</code> - Post last update time</summary>

Post last update time.

Retrieve the timestamp indicating the last update/change of the post, as unix time epoch.

##### Returns
**`int`** - UNIX Timestamp representing the post's last update/change.
</details>

<details>
<summary><code>content_type() -> str</code> - Get type of post data (e.g. gif, image etc.)</summary>

Get type of post data (e.g. gif, image etc.).

Represents the value of `file_type` from the api.

##### Returns
**`str`** - A string indicating the type of the post.
**Possible values**
- `image` Post is of an image.
- `gif` Post is of an animation (gif, webm, or other format).
- `video` Post is of a video.
</details>

<details>
<summary><code>directory() -> int</code> - Get directory id of post</summary>

Get directory id of post.

##### Returns
**`int`** - Unknown Data.
</details>

<details>
<summary><code>hash() -> str</code> - Obtain the unique hash of post</summary>

Obtain the unique hash of post.

##### Returns
**`str`** - The hash associated with the post.
</details>

<details>
<summary><code>id() -> int</code> - Obtain the unique identifier of post</summary>

Obtain the unique identifier of post.

##### Returns
**`int`** - The unique identifier associated with the post.
</details>

<details>
<summary><code>image() -> str</code> - Get the image of the post</summary>

Get the image of the post.

##### Returns
**`str`** - Image url for the post.
</details>

<details>
<summary><code>owner() -> str</code> - Get username of post creator</summary>

Get username of post creator.

##### Returns
**`str`** - Username of post creator.
</details>

<details>
<summary><code>rating() -> str</code> - Retrieve the content rating of the post</summary>

Retrieve the content rating of the post.

##### Returns
**`str`** - A string representing the post's rating.
**Possible Values:**
- `e` Explicit
- `s` Safe
- `q` Questionable
</details>

<details>
<summary><code>sample() -> str</code> - Get the sample image/video of the post</summary>

Get the sample image/video of the post.

##### Returns
**`str`** - Sample data url for the post.
</details>

<details>
<summary><code>score() -> int</code> - Get the score of post</summary>

Get the score of post.

##### Returns
**`int`** - The post's score.
</details>

<details>
<summary><code>size() -> list[int, int]</code> - Retrieve actual size of post's image</summary>

Retrieve actual size of post's image.

##### Returns
**`list[int, int]`** - List of [width, height] representing the image dimensions.
</details>

<details>
<summary><code>tags() -> list[str]</code> - Get tags of post</summary>

Get tags of post.

##### Returns
**`list[str]`** - List of posts tags.
</details>

<details>
<summary><code>thumbnail() -> str</code> - Get the thumbnail image of the post</summary>

Get the thumbnail image of the post.

##### Returns
**`str`** - Thumbnail url for the post.
</details>

<details>
<summary><code>video() -> str</code> - Get the video of the post</summary>

Get the video of the post.

##### Returns
**`str`** - Video url for the post.
</details>

## PostComment
PostComment

Class to represent a comment under a post.

### Functions

<details>
<summary><code>__init__(id: int, owner_id: int, body: str, post_id: int, creation: str)</code> - PostComment Class</summary>

PostComment Class

##### Parameters
| Parameter  | Type  |
|:-----------|:------|
| `id`       | `int` |
| `owner_id` | `int` |
| `body`     | `str` |
| `post_id`  | `int` |
| `creation` | `int` |
</details>

### Properties

<details>
<summary><code>author_id() -> int</code> - Id of the comments author</summary>

Id of the comments author.

##### Returns
**`int`** - Id of comment author.
</details>

<details>
<summary><code>body() -> str</code> - Content of the comment</summary>

Content of the comment.

##### Returns
**`str`** - Content of the comment.
</details>

<details>
<summary><code>creation() -> int</code> - Timestamp when the comment was created <b><u>[ATTENTION]</u></b></summary>

Timestamp when the comment was created.

**Important: currently rule34.xxx api returns the time *when your
api request was made* and _not_ the time when the comment was created.**

##### Returns
**`int`** - Timestamp when comment was created.
</details>

<details>
<summary><code>id() -> int</code> - Comments unique id</summary>

Comments unique id.

##### Returns
**`int`** - Comments unique id.
</details>

<details>
<summary><code>post_id() -> int</code> - Id of post, to whom the comment belongs</summary>

Id of post, to whom the comment belongs.

##### Returns
**`int`** - Id of parent post.
</details>

## Stat
Stat Class.

Generic Stat class, mostly used to Top nth lists.

### Functions

<details>
<summary><code>__init__(place: int, amount: int, username: str)</code> - Stat class</summary>

Stat class.

##### Parameters
| Parameter  | Type  |
|:-----------|:------|
| `place`    | `int` |
| `amount`   | `int` |
| `username` | `str` |
</details>

### Properties

<details>
<summary><code>amount() -> int</code> - Get amount/count of it</summary>

Get amount/count of it.

##### Returns
**`int`** - Amount of something related to this stat.
</details>

<details>
<summary><code>place() -> int</code> - Get index/positional place of the stat</summary>

Get index/positional place of the stat.

##### Returns
**`int`** - Positional index.
</details>

<details>
<summary><code>username() -> str</code> - Get username or name of character related to this stat</summary>

Get username or name of character related to this stat.

##### Returns
**`str`** - Related username / name of a character to this stat.
</details>

## TopTag
TopTag Class.

### Functions

<details>
<summary><code>__init__(rank: int, tagname: str, percentage: int)</code> - TopTag Class</summary>

TopTag Class.

##### Parameters
| Parameter    | Type  |
|:-------------|:------|
| `rank`       | `int` |
| `tagname`    | `str` |
| `percentage` | `int` |
</details>

<details>
<summary><code>__from_dict(json: dict) -> TopTag</code> - Create TopTag class from JSON data</summary>

Create TopTag class from JSON data.

##### Parameters
| Parameter | Type   | Description                         |
|:----------|:-------|:------------------------------------|
| `json`    | `dict` | JSON data from rule34.xxx REST Api. |

##### Returns
**`TopTag`** - TopTag object.
</details>

### Properties

<details>
<summary><code>percentage() -> int</code> - Get tags percentage in use</summary>

Get tags percentage in use.

##### Returns
**`int`** - Tags usage as percentage value.
</details>

<details>
<summary><code>rank() -> int</code> - Get tags rank</summary>

Get tags rank.

##### Returns
**`int`** - Get rank of the tag.
</details>

<details>
<summary><code>tagname() -> str</code> - Get tags name</summary>

Get tags name.

##### Returns
**`str`** - Get name of the tag.
</details>

## ICame
ICame Class.

ICame chart item.

### Functions

<details>
<summary><code>__init__(character_name: str, count: int)</code> - ICame Class</summary>

ICame Class.

iCame chart item.

##### Parameters
| Parameter        | Type  |
|:-----------------|:------|
| `character_name` | `str` |
| `count`          | `int` |
</details>

### Properties

<details>
<summary><code>character_name() -> str</code> - Get name of character</summary>

Get name of character.

##### Returns
**`str`** - Name of character.
</details>

<details>
<summary><code>count() -> int</code> - Get count of how often people came on the character</summary>

Get count of how often people came on the character.

##### Returns
**`int`** - Cum count.
</details>

<details>
<summary><code>tag_url() -> str</code> - Get url of tag</summary>

Get url of tag.

##### Returns
**`str`** - Url of tag.
</details>
