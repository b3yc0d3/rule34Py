class ICame:
    """ICame chart item
    """

    def __init__(self, character_name: str, count: int):
        """ICame chart item

        Args:
            character_name (str): Name of Character
            count (int): Came on character count
        """

        self._character_name = character_name
        self._tag_url = "https://rule34.xxx/index.php?page=post&s=list&tags={0}".format(character_name.replace(" ", "_"))
        self._count = count

    @property
    def character_name(self) -> str:
        """Get name of character

        Returns:
            str: Name of character
        """

        return self._character_name

    @property
    def tag_url(self) -> str:
        """Get tag url

        Returns:
            str: Tag url
        """

        return self._tag_url

    @property
    def count(self) -> int:
        """Get came count

        Returns:
            int: Cum count
        """

        return self._count
