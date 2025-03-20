#Импорт всех нужных классов
from src.mainprocesses.dead import DeadMenager
from src.processes.health import Health
from src.processes.hunger import Hunger
from src.processes.happy import Happy
from src.items.inventory import Inventory

from src.log.logger_config import  logger

#Импорт всех нужных библиотек
import threading
import random
import time

class Tamago:

    def __init__(self,name):



        self.name = name
        self.livest = 1

        #Инициализация классов
        self.health = Health(self.name)
        self.happy = Happy(self.name, self.health)
        self.hunger = Hunger(self.happy, self.health, self.name)

        self.inventory = Inventory(self.hunger, self.health, self.happy)

        #Установление нужных параметров (age будет использоваться не только тут поэтому она открытая)
        self.age = 0
        self.__maxAge = 100

    def Live(self):

        #Запуск всех процессов в разные потоки

        logger.info("запуск главных процессов")

        threading.Thread(target=self.Ageing, daemon=True).start()
        threading.Thread(target=self.DeadCheck, daemon=True).start()
        threading.Thread(target=self.hunger.Hung, daemon=True).start()
        threading.Thread(target=self.hunger.DeadFood, daemon=True).start()
        threading.Thread(target=self.health.Diseas, daemon=True).start()
        threading.Thread(target=self.happy.sad, daemon=True).start()



    def Ageing(self):
        logger.info("запуск старения")
        #Старение раз в 6 секунд на секунду
        while DeadMenager.alive():

            time.sleep(6)
            self.age += 1
            if self.age == self.__maxAge:
                DeadMenager.kill()

    def DeadCheck(self):
        logger.info("запуск проверки на смерть")
        #Проверка на смерть
        while DeadMenager.alive():
            if self.health.healthlv == 0:
                logger.info("смерть от потери здоровья")
                self.Dead()

            if self.hunger.weight == 0:
                logger.info("смерть от голода")
                self.Dead()

            if self.happy.happylv == 0:
                logger.info("смерть от грусти")
                self.Dead()


    def Dead(self):

        #Выбор случайной фразы после смерти
        self.__deadwords = ['умер', 'умер жестокой смертью','сдох','вы проиграли','press F']
        self.__deadst = random.randint(0, len(self.__deadwords))
        logger.info("вывод информации о смерти")
        print(self.__deadwords[self.__deadst-1])

        #Смерть
        DeadMenager.kill()