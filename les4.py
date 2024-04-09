#venv - виртуальное окружение
# модули - 1 вид встроенные модули

import random,time

# while 2:
#     print(random.randint(1,10))
#     time.sleep(3)

# import math
# print(math.pi)

from math import pi as numpi
# nampi=pi
# print(numpi)

# 2 вид модулей - собвственные модули

from lesson3 import BankBeka

p=BankBeka(1000000,1000000,1111)
p.getmoney



# from runnn import BankBeka

# from initt import p
# p.BankBeka


# 3 вид внешние модули - надо скачать
from art import tprint
import colorama
print(colorama.Back.LIGHTMAGENTA_EX,colorama.Fore.YELLOW,colorama.Style.DIM)
print('sdfghjk')
tprint('Hello World')


