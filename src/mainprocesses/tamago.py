# tamago.py (логика тамагочи)
from src.mainprocesses.dead import DeadMenager
from src.processes.health import Health
from src.processes.hunger import Hunger
from src.processes.happy import Happy
from src.items.inventory import Inventory
from src.log.logger_config import logger
import threading
import random
import time

class Tamago:
    def __init__(self, name):
        self.name = name
        self.livest = 1
        self.health = Health(self.name)
        self.happy = Happy(self.name, self.health)
        self.hunger = Hunger(self.happy, self.health, self.name)
        self.inventory = Inventory(self.hunger, self.health, self.happy)
        self.age = 0
        self.__maxAge = 100

    def Live(self):
        logger.info("Запуск главных процессов")
        threading.Thread(target=self.Ageing, daemon=True).start()
        threading.Thread(target=self.DeadCheck, daemon=True).start()
        threading.Thread(target=self.hunger.Hung, daemon=True).start()
        threading.Thread(target=self.hunger.DeadFood, daemon=True).start()
        threading.Thread(target=self.health.Diseas, daemon=True).start()
        threading.Thread(target=self.happy.sad, daemon=True).start()

    def Ageing(self):
        logger.info("Запуск старения")
        while DeadMenager.alive():
            time.sleep(6)
            self.age += 1
            if self.age == self.__maxAge:
                DeadMenager.kill()

    def DeadCheck(self):
        logger.info("Запуск проверки на смерть")
        while DeadMenager.alive():
            if self.health.healthlv <= 0:
                logger.info("Смерть от потери здоровья")
                self.Dead()
            if self.hunger.weight <= 0:
                logger.info("Смерть от голода")
                self.Dead()
            if self.happy.happylv <= 0:
                logger.info("Смерть от грусти")
                self.Dead()
            time.sleep(1)

    def Dead(self):
        self.__deadwords = ['умер', 'умер жестокой смертью', 'сдох', 'вы проиграли', 'press F']
        print(random.choice(self.__deadwords))
        DeadMenager.kill()