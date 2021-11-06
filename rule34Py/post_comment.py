class PostComment:
    def __init__(self, id: int, owner_id:int, body: str, post_id: int, creation: str):
        """Post Comment
        """
        self._id = id
        self._owner_id = owner_id
        self._body = body
        self._post_id = post_id
        self._creation = creation

    @property
    def id(self) -> int:
        """Id of comment
        Returns:
            int: Id of comment
        """
        return self._id

    @property
    def author_id(self) -> int:
        """Id of comment author
        Returns:
            int: Id of author
        """
        return self._owner_id

    @property
    def body(self) -> str:
        """Comment content
        Returns:
            str: Body of comment
        """
        return self._body

    @property
    def post_id(self) -> int:
        """Id of parent post
        Returns:
            int: Id of parent post
        """
        return self._post_id

    @property
    def creation(self) -> str:
        """Timestamp of creation
        Returns:
            str: Creation Timestamp
        """
        return self._creation
