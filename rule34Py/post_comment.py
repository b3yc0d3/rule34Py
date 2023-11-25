class PostComment:
    """
    PostComment

    Class to represent a comment under a post.
    """

    def __init__(self,
            id: int,
            owner_id: int,
            body: str,
            post_id: int,
            creation: str):
        """
        Post Comment

        :param id: Comments id.
        :type id: int

        :param owner_id: Comment creators id.
        :type owner_id: int

        :param body: Content/body of the comment.
        :type body: str

        :param post_id: Id of post to whom the comment belongs.
        :type post_id: int

        :param creation: Time when the comment was created.
        :type creation: str
        """
        self._id = id
        self._owner_id = owner_id
        self._body = body
        self._post_id = post_id
        self._creation = creation

    @property
    def id(self) -> int:
        """
        Comments unique id.

        :return: Comments unique id.
        :rtype: int
        """
        return self._id

    @property
    def author_id(self) -> int:
        """
        Id of the comments author.

        :return: Id of comments author.
        :rtype: int
        """

        return self._owner_id

    @property
    def body(self) -> str:
        """
        Content of the comment.

        :return: Content of the comment.
        :rtype: str
        """
        return self._body

    @property
    def post_id(self) -> int:
        """
        Id of post, to whom the comment belongs.

        :return: Id of parent post.
        :rtype: int
        """
        
        return self._post_id

    @property
    def creation(self) -> str:
        """
        Timestamp of when the comment was created.

        **Important: currently rule34.xxx api returns the time *when your
        api request was made* and _not_ the time when the comment was created.**

        :return: Timestamp when comment was created.
        :rtype: str
        """
        
        return self._creation
