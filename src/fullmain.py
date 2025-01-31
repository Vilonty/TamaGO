"""

ЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫ
ПОЛНАЯ НЕДЕЛИМАЯ ВЕРСИЯ КОДА
ЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫ

import time
import threading
import random
import abc


class Edible(abc.ABC):
    @abc.abstractmethod
    def setPoints(self, *args): pass



class Pills(Edible):
    pillslist = [["Таблетка 1", 0],
                 ["Таблетка 2", 5]]

    @staticmethod
    def setPoints(num):

        return Pills.pillslist[num-1][1]


class Health:

    def __init__(self):

        self.healthlv = 100
        self.healthst = 1
        self.__dieseasch = 1

    def Diseas(self):


        while DeadMenager.alive():

            time.sleep(10)
            self.__ch = random.randint(self.__dieseasch,10)

            if self.__ch > 7:

                self.healthst = 0
                print("\nВы заболели")

                while self.healthst == 0:
                    time.sleep(10)
                    self.healthlv -= 1

    def Regen(self):

        self.pillsnum = input("\nВведите номер таблетки (1-2) \nВернуться назад: b  ")

        if self.pillsnum == "b".lower():
            pass

        try:
            self.pillsnum = int(self.pillsnum)
            if self.pillsnum in range(1, 3):

                self.healthlv += Pills.setPoints(self.pillsnum)

                if self.healthlv > 100: self.healthlv = 100

                print("\nВы выздоровели! "
                      "\nУровень здоровья: ", self.healthlv)
                self.healthst = 1

        except:

            print("Команда введена неверно")
            self.Regen()


class Food(Edible):
    foodlist = [["Еда 1", 5, 2], ["Еда 2", 6, 2], ["Еда 3", 10, 2]]

    @staticmethod
    def setPoints(num, pnum):
        return Food.foodlist[num - 1][pnum]




class Hunger:

    def __init__(self, happy, health):

        self.happy = happy
        self.health = health

        self.weight = 100
        self.obestylv = 0

    def Hung(self):

        while DeadMenager.alive():

            time.sleep(2)
            self.weight -= 1

            if self.weight > 100:
                self.obestylv -= 1

    def Eat(self):

        self.foodtype = input('\nВведите номер нужной еды (1-3) \nВернуться: b ')

        if self.foodtype == 'b'.lower():
            pass

        try:
            self.foodtype = int(self.foodtype)

            if self.foodtype in range(1, 4):

                self.weight += Food.setPoints(self.foodtype, 1)

                if self.weight > 100:

                    self.Obesty()

                self.happy.happylv += Food.setPoints(self.foodtype, 2)
        except:

            print('\nКомманда введена неверно')
            self.Eat()




    def Obesty(self):

        self.obestylv = self.weight - 100

    def DeadFood(self):

        while DeadMenager.alive():
            if self.weight == 0:

                self.health.healthlv = 0


class Happy:

    def __init__(self):

        self.happylv = 50
        self.happymax = 100
        self.__face = 3

    def sad(self):

        while DeadMenager.alive():
            time.sleep(5)
            self.happylv -= 1


class DeadMenager:
    livest = 1

    @staticmethod
    def kill():
        DeadMenager.livest = 0
        exit()

    @staticmethod
    def alive():
        return DeadMenager.livest


class Tamago:

    def __init__(self,name):

        self.name = name
        self.livest = 1

        self.health = Health()
        self.happy = Happy()
        self.hunger = Hunger(self.happy, self.health)

        self.age = 0
        self.__maxAge = 100

    def Live(self):

        threading.Thread(target=self.Ageing, daemon=True).start()
        threading.Thread(target=self.DeadCheck, daemon=True).start()
        threading.Thread(target=self.hunger.Hung, daemon=True).start()
        threading.Thread(target=self.hunger.DeadFood, daemon=True).start()
        threading.Thread(target=self.health.Diseas, daemon=True).start()
        threading.Thread(target=self.happy.sad, daemon=True).start()



    def Ageing(self):

        while DeadMenager.alive():

            time.sleep(6)
            self.age += 1
            if self.age == self.__maxAge:
                DeadMenager.kill()

    def DeadCheck(self):

        while DeadMenager.alive():
            if self.health.healthlv == 0:
                self.Dead()

            if self.hunger.weight == 0:
                self.Dead()

            if self.happy.happylv == 0:
                self.Dead()


    def Dead(self):

        self.__deadwords = ['умер', 'умер жестокой смертью','сдох','вы проиграли','press F']
        self.__deadst = random.randint(0, len(self.__deadwords))
        print(self.__deadwords[self.__deadst-1])
        DeadMenager.kill()




class UI:

    def __init__(self):

        self.name = input('введите имя: ')
        self.tamago = Tamago(self.name)
        self.Display()

    def Display(self):

        print('\nИмя питомца: ', self.name)
        self.tamago.Live()
        self.Game()

    def Game(self):

        while DeadMenager.alive():

            self.move = input("\nВведите действие: "
                              "\nУзнать информацию [1], "
                              "\nПокормить [2], "
                              "\nВылечить [3], "
                              "\nЗакончить игру [ext] ").lower()

            if self.move == "1":

                print("\nВозраст: ", self.tamago.age,
                      " \nЗдоровье: ", self.tamago.health.healthlv,
                      " \nВес: ", self.tamago.hunger.weight,
                      " \nОжирение: ", self.tamago.hunger.obestylv,
                      " \nРадость: ", self.tamago.happy.happylv,
                      f" \nБолезнь: {'да' if self.tamago.health.healthst == 0 else 'нет'}")

            elif self.move == "2":

                self.tamago.hunger.Eat()

                print("\nВы покормили ", self.name,
                      "\nВес: ", self.tamago.hunger.weight,
                      "\nОжирение: ", self.tamago.hunger.obestylv,
                      "\nРадость: ", self.tamago.happy.happylv)

            elif self.move == "3":

                if self.tamago.health.healthst == 1:

                    print("\nЛечение не нужно")

                else:

                    self.tamago.health.Regen()

            elif self.move == "ext":

                self.tamago.Dead()

            else:

                print("\nКоманда введена неверно")


start = UI()
"""