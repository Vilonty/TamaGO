from src.items.food import Food
from src.mainprocesses.dead import DeadMenager
import time
class Hunger:

    def __init__(self, happy, health, name):

        self.happy = happy
        self.health = health
        self.name = name

        self.weight = 100
        self.obestylv = 0

    def Hung(self):

        #Процесс голодания
        while DeadMenager.alive():

            time.sleep(2)
            self.weight -= 1

            if self.weight > 100:
                #Получение информации о излишнем весе
                self.obestylv -= 1

    def Eat(self):

        #Возможность кормить
        self.foodtype = input('\nВведите номер нужной еды (1-3) \nВернуться: b ')

        if self.foodtype.lower() == 'b':
            # Если пользователь вводит b то функция выключается
            return

        #Моя жалкая высосанная из пальца сделать обработку исключений
        try:
            #Если человек вводит числа от 1 до 3х включетльно, то выбирается номер нужной еды
            self.foodtype = int(self.foodtype)

            if self.foodtype in range(1, 4):

                #Так как класс food статичный, можем его как хотим использовать
                self.weight += Food.setPoints(self.foodtype, 1)

                if self.weight > 100:

                    self.Obesty()

                #Добавление счастья
                self.happy.happylv += Food.setPoints(self.foodtype, 2)

                #Вывод информации о команде
                print("\nВы покормили ", self.name,
                      "\nВес: ", self.weight,
                      "\nОжирение: ", self.obestylv,
                      "\nРадость: ", self.happy.happylv)

            else:
                print('Неправильный номер еды')
                self.Eat()

        except:
            #Если пользователь ввёл фигню какую-то то ничо не сработает
            print('Неправильное значение')
            self.Eat()



    def Obesty(self):
        #функция ожирения
        self.obestylv = self.weight - 100

    def DeadFood(self):

        #В случае если голод закончится, запускается смерть
        while DeadMenager.alive():
            if self.weight == 0:

                self.health.healthlv = 0