from src.items.pills import Pills
from src.mainprocesses.dead import DeadMenager
import time
import random

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