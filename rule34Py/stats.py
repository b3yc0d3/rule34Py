class Stat:
    """
    Stat class

    Generic Stat class, mostly used to Top nth lists.
    """
    def __init__(self, place, amount, username):
        """
        Stat class.

        :param place: Positional index.
        :type place: int
        
        :param amount: Count of something.
        :type amount: int

        :param username: Name, either a "username" or a charters name.
        :type username: str
        """

        self.__place = place
        self.__amount = amount
        self.__username = username

    @property
    def place(self):
        """
        Get positional place of the stat.

        :return: Positional index.
        :rtype: int
        """
        return self.__place

    @property
    def amount(self):
        """
        Get amount/count of it.

        :return: Amount of something related to this stat.
        :rtype: int
        """
        return self.__amount

    @property
    def username(self):
        """
        Get username or name of character related to this stat.

        :return: Related username / name of a character to this stat.
        :rtype: str
        """
        return self.__username
