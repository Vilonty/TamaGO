'''
ЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫ
Я не нашёл ни одного места в программе, где у меня экземпляры класса взаимодействовали бы
между собой, поэтому вынес это сюда чтобы показать что я умею это делать и разобрался, тут просто x и y скалдываются
выводятся и всё такое
ЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫ



class main:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):

        return 'main({}, {})'.format(self.x, self.y)

    def __str__(self):

        return '({}, {})'.format(self.x, self.y)

    def __eq__(self, other):

        return (self.x == other.x) and (self.y == other.y)

    def __gt__(self,other):

        return (self.x > other.x) and (self.y > other.y)

    def __add__(self, other):

        return main(self.x + other.x, self.y + other.y)

x = main(1,2)
y = main(2,3)
print(x)
print(y)

print(x + y)

print(x == y)

print(x > y)
print(x < y)

'''
import random

'''задание 1:
from src.over.Error import err


class BaseError(Exception):
    def __init__(self, message="ошибка"):
        super().__init__(message)

    def __str__(self):

        return self.args[0]

class CustomError(BaseError):
    def __init__(self, message="ошибка2"):
        super().__init__(message)

class SpecificError(CustomError):
    def __init__(self, message="ошибка3"):
        super().__init__(message)

class ErrorTest:
    @staticmethod
    def Choise():

        a = int(input('введите номер (1-4) ошибки которую хотите получить (зачем? а фиг знает) '))


        if a == 1:
            ErrorTest.err1()
        elif a == 2:
            ErrorTest.err2()
        elif a == 3:
            ErrorTest.err3()
        elif a ==4:
            ErrorTest.err4()

    @staticmethod
    def err1():
        raise BaseError('Ы')

    @staticmethod
    def err2():
        raise CustomError('ыы')

    @staticmethod
    def err3():
        raise SpecificError('ыыы')

    @staticmethod
    def err4():
        raise err('Неправильное значение')


class Test:
    @staticmethod
    def Go():

        a = 1
        b = 0

        try:

            a / b

        except:

            b / 1

        finally:
            f = open('lyris.txt', 'r')
            pog = f.read()
            print(pog)
            ErrorTest.Choise()


Test.Go()
'''
'''
задание 2:
class Test23:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f"{self.a} {self.b}"


d = []

d = [Test23('aaa1','fff'),
     Test23('aaa1','fff'),
     Test23('aaa1','fff'),
     Test23('aaa1','fff'),
     Test23('aaa1','fff')]

print(d[1])

d1 = [
    [Test23('a', 1), Test23('a', 2)],
    [Test23('a', 3), Test23('b', 4)],
    [Test23('v', 5), Test23('b', 6)]
]



class Test24:
    @staticmethod
    def mass(mass):

        if not mass:
            print("пусто")
            return

        a = input('введите значение атрибута ')
        d3 = None



        for i in range(len(mass)):
            for j in range(len(mass[i])):
                if mass[i][j].a == a:
                    d3 = mass[i][j]
                    if j + 1 < len(mass[i]) and mass[i][j].b < mass[i][j + 1].b:
                        d3 = mass[i][j]


        if d3 is not None:
            print(d3)
        else:
            print('вы ввели неправильный атрибут')

Test24.mass(d1)

'''

'''
3/4/5
class one:
    def __init__(self):
        self._property1 = 'я защищённое чмо'

    def alert(self):
        print('ы')

    def alert2(self):
        print('ы2')

    def alert3(self):
        print('ы3')

import  random
class two(one):
    def __init__(self):
        super().__init__()

    def alert(self):
        super().alert()
        print('e')

    def alert2(self):
        print('e2')

    def alert4(self):
        a = random.randint(1,2)
        if a == 1:
            self.alert2()
            super().alert2()
        else:
            super().alert2()
            self.alert2()

    def alert5(self):

        print(self._property1)




t = two()

t.alert()
t.alert2()
t.alert3()
t.alert4()
t.alert5()
'''



class Bibibi:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):

        return f"Bibibi(name='{self.name}', age={self.age})"

    def __repr__(self):

        return f"Bibibi(name='{self.name}', age={self.age})"



bi = Bibibi("ыЫы", 10)

print(str(bi))
print(repr(bi))

new_bi = eval(repr(bi))
print(new_bi)
