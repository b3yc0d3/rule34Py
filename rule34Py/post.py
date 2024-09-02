""""""
"""
rule34Py - Python api wrapper for rule34.xxx

Copyright (C) 2022-2024 b3yc0d3 <b3yc0d3@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

"""
TODO: Restructure internal variable names
"""

class Post:
    
    @staticmethod
    def from_json(json):        
        pFileUrl = json["file_url"]
        pHash = json["hash"]
        pId = json["id"]
        pScore = json["score"]
        pSize = [json["width"], json["height"]]
        pOwner = json["owner"]
        pTags = json["tags"].split(" ")
        preview = json["preview_url"]
        sample = json["sample_url"] # thumbnail
        change = json["change"]
        directory = json["directory"]
        
        img_type = "video" if pFileUrl.endswith(".mp4") else "gif" if pFileUrl.endswith(".gif") else "image"
            
        return Post(pId, pHash, pScore, pSize, pFileUrl, preview, sample, pOwner, pTags, img_type, directory, change)
    
    def __init__(self, id: int, hash: str, score: int, size: list, image: str, preview: str, sample: str, owner: str, tags: list, file_type: str, directory: int, change: int):
        self._file_type = file_type
        self._video = ""
        self._image = ""
        
        if file_type == "image" or file_type == "gif":
            self._image = image
        elif file_type == "video":
            self._video = image
        
        self._id = id
        self._hash = hash
        self._score = score
        self._size = size # > [WIDTH:int, HEIGHT:int]
        self._preview = preview # thumbnail
        self._sample = sample
        self._owner = owner
        self._tags = tags # > [TAG:str, TAG:str,...]
        self._directory = directory
        self._change = change
        self._rating = None
        

    @property
    def id(self) -> int:
        """
        Obtain the unique identifier of post.

        :return: The unique identifier associated with the post.
        :rtype: int
        """
        return self._id

    @property
    def hash(self) -> str:
        """
        Obtain the unique hash of post.

        :return: The hash associated with the post.
        :rtype: str
        """
        return self._hash

    @property
    def score(self) -> int:
        """
        Get the score of post.
        
        :return: The post's score.
        :rtype: int
        """
        return self._score

    @property
    def size(self) -> list:
        """
        Retrieve actual size of post's image.
        
        :return: List of [width, height] representing the image dimensions.
        :rtype: list[int, int]
        """
        return self._size

    @property
    def rating(self) -> str:
        """
        Retrieve the content rating of the post.

        :return: A string representing the post's rating.
            - 'e' Explicit
            - 's' Safe
            - 'q' Questionable
        :rtype: str
        """
        return self._rating

    @property
    def image(self) -> str:
        """
        Get the image of the post.

        :return: Image url for the post.
        :rtype: str
        """

        return self._image
    
    @property
    def video(self) -> str:
        """
        Get the video of the post.

        :return: Video url for the post.
        :rtype: str
        """

        return self._video
    
    @property
    def thumbnail(self) -> str:
        """
        Get the thumbnail image of the post.

        :return: Thumbnail url for the post.
        :rtype: str
        """

        return self._preview
    
    @property
    def sample(self) -> str:
        """
        Get the sample image/video of the post.

        :return: Sample data url for the post.
        :rtype: str
        """

        return self._sample

    @property
    def owner(self) -> str:
        """
        Get username of post creator.
            
        :return: Username of post creator.
        :rtype: str
        """

        return self._owner

    @property
    def tags(self) -> list:
        """
        Get tags of post.

        :return: List of posts tags
        :rtype: list[str]
        """

        return self._tags

    @property
    def content_type(self) -> str:
        """
        Get type of post data (e.g. gif, image etc.)

        Represents the value of ``file_type`` from the api.
        
        :return: A string indicating the type of the post.
            Possible values:
        
            - 'image': Post is of an image.
            - 'gif': Post is of an animation (gif, webm, or other format).
            - 'video': Post is of a video.
        :rtype: str
        """
        
        return self._file_type
    
    @property
    def change(self) -> int:
        """
        Post last update time

        Retrieve the timestamp indicating the last update/change of
        the post, as unix time epoch.

        :return: UNIX Timestamp representing the post's last update/change.
        :rtype: int
        """
        
        return self._change
    
    @property
    def directory(self) -> int:
        """
        Get directory id of post

        :return: Unknown Data
        :rtype: int
        """
        
        return self._directory