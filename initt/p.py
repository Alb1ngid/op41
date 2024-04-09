class BankBeka:

    def __init__(self, name, key, money):
        self.name = name
        self._key = key
        self.__money = money

    @property
    def getmoney(self):
        return self.__money
    @getmoney.setter
    def getmoney(self, money):
        self.__money = money
    @getmoney.deleter
    def getmoney(self):
        del self.__money

    def __str__(self):
        return f'{self.name} {self.__money}'