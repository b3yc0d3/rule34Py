class TopTag:
    """
    TopTag class
    """

    def __init__(self, rank: int, tagname: str, percentage: int):
        """
        TopTag class.

        :param rank: Rank of the tag.
        :type rank: int

        :param tagname: Name of the tag.
        :type tagname: str

        :param percentage: Percentage of how often tag is used.
        :type percentage: int
        """

        self._rank = rank
        self._tagname = tagname
        self._percentage = percentage
    
    def __from_dict(json: dict):
        """
        Create TopTag class from JSON data.

        :return: TopTag object.
        :rtype: TopTag
        """
        return TopTag(json["rank"], json["tagname"], json["percentage"] * 100)
        
    @property
    def rank(self) -> int:
        """
        Get tags rank.

        :return: Get rank of the tag.
        :rtype: int
        """

        return self._rank
    
    @property
    def tagname(self) -> str:
        """
        Get tags name.

        :return: Get name of the tag.
        :rytpe: str
        """

        return self._tagname
    
    @property
    def percentage(self) -> int:
        """
        Get tags percentage in use.

        :return: Tags usage as percentage value.
        :rtype: int
        """

        return self._percentage