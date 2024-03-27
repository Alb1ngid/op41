# ООП
# сlass

type_python = '1' #'werd',1.8778,True,None,[],{},()
type_python.isalpha()

# print(type(type_python))

class Human:
    body='True'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # методы
    def printt(self):
        print('привет ',self.body)

    #маг метод
    def __str__(self):
        return (f'name: {self.name} \n'
                f'age: {self.age}')
    def __len__(self):
        return len(self.body)


# объект класса \экземпляр класса
beka=Human('beka',20)
# beka.printt()

ainura=Human('ainura',80)

# print(len(beka))
print(ainura)



#

