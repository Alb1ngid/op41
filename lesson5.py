

# '''python -m venv beka'''
'''env/Scripts/activate'''
'''pip install'''
'''pip freeze '''
'''pip freeze > requirements.txt'''
'''pip install -r requirements.txt'''


# МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ

class A:
    def  __init__(self,a):
        self.a=a


class A2(A):
    def __str__(self):
        return self.a
class B:
    def __init__(self,b):
        self.b=b
    def __str__(self):
        return 'Hello World'

class C(B,A2):
    def __init__(self,a,b):
        A.__init__(self,a)
        B.__init__(self,b)

# mro-порядок населдование методов
c=C('beka','qwert')
print(c)
print(C.mro())
