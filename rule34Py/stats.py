class Stat:
    def __init__(self, place, amount, username):
        self.__place = place
        self.__amount = amount
        self.__username = username

    @property
    def place(self):
        return self.__place

    @property
    def amount(self):
        return self.__amount

    @property
    def username(self):
        return self.__username
