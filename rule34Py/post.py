class Post:
    def __init__(self, id: int, hash: str, score: int, size: list, image: str, owner: str, tags: list):
        self._id = id
        self._hash = hash
        self._score = score
        self._size = size # > [WIDTH:int, HEIGHT:int]
        self._image = image
        self._owner = owner
        self._tags = tags # > [TAG:str, TAG:str,...]

    @property
    def id(self) -> int:
        """Get id of post
        Returns:
            int: Id of Post
        """
        return self._id

    @property
    def hash(self) -> str:
        """Get hash of post
        Returns:
            str: Hash of Post
        """
        return self._hash

    @property
    def score(self) -> int:
        """Get score of post
        Returns:
            int: Score of post
        """
        return self._score

    @property
    def size(self) -> list:
        """Get image size
        Returns:
            list: Returns a list of to integers (eg: [1920, 1080] > [WIDTH, HEIGHT])
        """
        return self._size

    @property
    def image(self) -> str:
        """Get post image
        Returns:
            list: Image url
        """

        return self._image

    @property
    def owner(self) -> str:
        """Get username of post creator
        Returns:
            str: Name of owner
        """

        return self._owner

    @property
    def tags(self) -> list:
        """Get tags of post
        Returns:
            list: String list of tags
        """

        return self._tags
