class ICame:
    """
    ICame chart item
    """

    def __init__(self, character_name: str, count: int):
        """
        iCame chart item.

        :param character_name: Name of the character.
        :type character_name: str

        :param count: Count of how often people came on the character.
        :type count: int
        """

        self._character_name = character_name
        self._tag_url = "https://rule34.xxx/index.php?page=post&s=list&tags={0}".format(character_name.replace(" ", "_"))
        self._count = count

    @property
    def character_name(self) -> str:
        """
        Get name of character.

        :return: Name of character.
        :rtype: str
        """

        return self._character_name

    @property
    def tag_url(self) -> str:
        """
        Get url of tag.

        :return: Url of tag.
        :rtype: str
        """

        return self._tag_url

    @property
    def count(self) -> int:
        """
        Get count of how often people came on the character.

        :return: Cum count
        :rtype: int
        """

        return self._count
