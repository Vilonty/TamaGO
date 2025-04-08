from src.items.ediblefabric import EdibleFactory
from src.log.logger_config import  logger
from src.mainprocesses.dead import DeadMenager
import time
import random

class Health:

    def __init__(self, name):

        self.name = name

        self.healthlv = 100
        self.healthst = 1
        self.__dieseasch = 1

    def Diseas(self):
        logger.info("запуск риска болезни")
        while DeadMenager.alive():
            time.sleep(10)
            if DeadMenager.alive() and random.randint(1, 10) > 7:
                self.healthst = 0
                print("\nВы заболели")
                while DeadMenager.alive() and self.healthst == 0:
                    time.sleep(10)
                    self.healthlv -= 1
                    if self.healthlv <= 0:
                        DeadMenager.kill()
                        break

    def Regen(self, item_id):
        logger.info("запуск процесса регенерации")
        try:

            pills_id = int(item_id)
            edible = EdibleFactory.create_edible('pills')

            pills_item = next((item for item in edible.getpillslist() if item['id'] == pills_id), None)


            if pills_item['col'] == 0:
                logger.info("ошибка регенирации: нет таблеток")
                print("Таблеток нет")
                return


            self.healthlv += pills_item["points"]

            if self.healthlv > 100: self.healthlv = 100

            pills_item['col'] -= 1

            logger.info(f"успешная регенирация, текущее количетсво хп: {pills_item['col']}, состояние здоровья: {self.healthlv}")
            print("\nВы вылечили", self.name, "!"
                  "\nУровень здоровья: ", self.healthlv)
            self.healthst = 1

        except ValueError:
            logger.info("неправльно введёная команда")
            print("Команда введена неверно")
            self.Regen()