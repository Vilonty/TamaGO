from src.mainprocesses.dead import DeadMenager
from src.items.ediblefabric import EdibleFactory
from src.log.logger_config import  logger
import time
class Happy:

    def __init__(self, name, health):

        self.happylv = 50
        self.happymax = 100

        #face пока не используется
        self.__face = 3

        self.name = name
        self.health = health


    def overjoy(self, item_id):

        logger.info("запуск приёма наркотиков")
        try:

            drug_id = int(item_id)
            edible = EdibleFactory.create_edible('drug')

            drug_items = next((item for item in edible.getdrugslist() if item['id'] == drug_id), None)

            self.happylv += drug_items["quantity"]

            if self.happylv > 100: self.happylv = 100

            drug_items['col'] -= 1

            self.health.healthlv -= 60
            logger.info(f"успешное применение наркотиков, текущее состояние счастья: {self.happylv} здоровья: {self.health.healthlv}")
            print("\nВы осчастливили", self.name, "!"
                  "\nУровень счастья: ", self.happylv)

        except ValueError:
            logger.info("неправльно введёная команда")
            print("Команда введена неверно")
            self.overjoy()

    def sad(self):
        logger.info("запуск грусти")
        #Грусть
        while DeadMenager.alive():
            time.sleep(5)
            self.happylv -= 1