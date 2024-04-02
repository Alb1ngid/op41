# инкапсуляция - сет гет делит
#  git clone - воровать проекты
# уровни защиты 3
# публичный - 0
# защищенный :_
# приватный - скрытый


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


class Account(BankBeka):
    def names(self):
        print(f'мое имя {self.name}')


ac0=Account('beka','12rge3',1000)
print(ac0.getmoney)
ac0.getmoney=100000
print(ac0.getmoney)
print(ac0)


