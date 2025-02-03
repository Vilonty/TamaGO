from src.mainprocesses.dead import DeadMenager
from src.processes.health import Health
from src.processes.hunger import Hunger
from src.processes.happy import Happy

import threading
import random
import time


class Tamago:

    def __init__(self,name):

        self.name = name
        self.livest = 1

        self.health = Health(self.name)
        self.happy = Happy()
        self.hunger = Hunger(self.happy, self.health, self.name)

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