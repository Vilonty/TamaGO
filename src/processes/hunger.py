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

        while DeadMenager.alive():

            time.sleep(2)
            self.weight -= 1

            if self.weight > 100:
                self.obestylv -= 1
    def Eat(self):

        self.foodtype = input('\nВведите номер нужной еды (1-3) \nВернуться: b ')

        if self.foodtype.lower() == 'b':
            return

        try:
            self.foodtype = int(self.foodtype)

            if self.foodtype in range(1, 4):

                self.weight += Food.setPoints(self.foodtype, 1)

                if self.weight > 100:

                    self.Obesty()

                self.happy.happylv += Food.setPoints(self.foodtype, 2)

                print("\nВы покормили ", self.name,
                      "\nВес: ", self.weight,
                      "\nОжирение: ", self.obestylv,
                      "\nРадость: ", self.happy.happylv)
        except:

            print('\nКомманда введена неверно')
            self.Eat()


    def Obesty(self):

        self.obestylv = self.weight - 100

    def DeadFood(self):

        while DeadMenager.alive():
            if self.weight == 0:

                self.health.healthlv = 0