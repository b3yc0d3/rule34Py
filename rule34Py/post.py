# rule34Py - Python api wrapper for rule34.xxx
# 
# Copyright (C) 2022-2025 b3yc0d3 <b3yc0d3@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""A module for representing Rule34 Post objects."""

# TODO: Restructure internal variable names


class Post:
    """A Rule34 Post object.

    This class is mostly a pythonic representation of the Rule34.xxx JSON API post object.

    Parameters:
        id: The Post's Rule34 ID number.
        hash: The Post's Rule34 object hash.
        score: The Post's voted user score.
        size: A two-element list of image dimensions. [width, height]
        image: URL to the Post's rule34 image server location.
        preview: A URL to the Post's preview image.
        sample: A URL to the Post's sample image.
        owner: The user who owns the Post.
        tags: A list of tags to assign to the Post.
        file_type: The Post's image file type. One of ["image", "gif", "video"].
        directory: The Post's image directory on the Rule34 image server.
        change: The Post's change ID.
    """

    @staticmethod
    def from_json(json: str) -> "Post":
        """Initialize a Post object from an ``api.rule34.xxx`` JSON Post element.

        Args:
            json: The JSON string to parse.
        
        Returns:
            The rule34Py.Post representation of the object.
        """
        pFileUrl = json["file_url"]
        pHash = json["hash"]
        pId = json["id"]
        pScore = json["score"]
        pSize = [json["width"], json["height"]]
        pOwner = json["owner"]
        pTags = json["tags"].split(" ")
        preview = json["preview_url"]
        sample = json["sample_url"]
        change = json["change"]
        directory = json["directory"]
        
        img_type = "video" if pFileUrl.endswith(".mp4") else "gif" if pFileUrl.endswith(".gif") else "image"
            
        return Post(pId, pHash, pScore, pSize, pFileUrl, preview, sample, pOwner, pTags, img_type, directory, change)
    
    def __init__(self, id: int, hash: str, score: int, size: list, image: str, preview: str, sample: str, owner: str, tags: list, file_type: str, directory: int, change: int):
        """Create a new Post object."""
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
        self._size = size
        self._preview = preview
        self._sample = sample
        self._owner = owner
        self._tags = tags
        self._directory = directory
        self._change = change
        self._rating = None
        

    @property
    def id(self) -> int:
        """The unique numeric identifier of post.

        Returns:
            The unique numeric identifier associated with the post.
        """
        return self._id

    @property
    def hash(self) -> str:
        """The unique rule34 hash of post.

        Returns:
            The hash associated with the post.
        """
        return self._hash

    @property
    def score(self) -> int:
        """Get the score of post.
        
        Returns:
            The post's score.
        """
        return self._score

    @property
    def size(self) -> list[int]:
        """The Post's graphical dimension size.
        
        Returns:
            A list of the image's graphical dimensions, as [width, height].
        """
        return self._size

    @property
    def rating(self) -> str:
        """The Post's content objectionability rating.

        Returns:
            A string representing the post's rating.
                - ``e`` = Explicit
                - ``s`` = Safe
                - ``q`` = Questionable
        """
        return self._rating

    @property
    def image(self) -> str:
        """The Post's full-resolution image URL.

        Returns:
            A string URL to the full-resolution image of the Post.
        """
        return self._image
    
    @property
    def video(self) -> str:
        """The Post's full-resolution video URL.

        Returns:
            A string URL to the full-resolution video URL.
        """
        return self._video
    
    @property
    def thumbnail(self) -> str:
        """The Post's thumbnail image URL.

        Returns:
            A string URL to the Post's thumbnail image.
        """
        return self._preview
    
    @property
    def sample(self) -> str:
        """The Post's sample image URL.

        Returns:
            A string URL to the sample image.
        """
        return self._sample

    @property
    def owner(self) -> str:
        """The Post's creator username.

        Returns:
            The string username of the Post creator.
        """
        return self._owner

    @property
    def tags(self) -> list:
        """The Post's tags.

        Returns:
            A List of the Post's tags.
        """
        return self._tags

    @property
    def content_type(self) -> str:
        """The Post's content type.

        Represents the value of ``file_type`` from the JSON.

        Returns:
            A string indicating the Post's content type.
                - ``image``: A static image.
                - ``gif``: An animated image (gif, webm, or other format).
                - ``video``: A video file.
        """
        return self._file_type

    @property
    def change(self) -> int:
        """The Post's latest update time.

        Returns:
            An int representing the UNIX timestamp of the Post's latest update/change.
        """
        return self._change

    @property
    def directory(self) -> int:
        """The Post's storage directory id.

        Returns:
            A numeric representation of the Post's storage directory.
        """
        return self._directory
