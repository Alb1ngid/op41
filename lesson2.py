# принципы ооп - Наследование пoлиморфизм обстракция инкапсуляция
# gitignore


# супер класс\родительский класс
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __len__(self):

    def __str__(self):
        return (f'меня зовут {self.name}\n'
                f'мне {self.age} лет')

    def oldplus(self, *args, **kwargs):
        ...

person1 = Person('айдай', 80)
print(person1)
person1.oldplus(100)
print(person1)

# дочерний класс
class Person2(Person):

    def oldplus(self):
        self.age+=40

    def old(self):
        self.age-=20



    def f(self,other):
        super().oldplus(other)

    def __init__(self, name, age, lastname):
        # Person.__init__(self,name,age)
        super().__init__(name,age)
        self.lastname = lastname

    def __str__(self):
        return f'{super().__str__()} {self.lastname}'


p=Person2('бека ', 69,'ndhsjeaf')
print(p)
p.oldplus()
p.f(10000)
print(p)
# p.old()
# print(p)

print(Person2.mro())