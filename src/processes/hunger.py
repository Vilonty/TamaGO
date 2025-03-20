from src.mainprocesses.dead import DeadMenager
import time
from src.items.ediblefabric import EdibleFactory
from src.log.logger_config import logger
class Hunger:
    def __init__(self, happy, health, name):
        self.happy = happy
        self.health = health
        self.name = name
        self.weight = 100
        self.obestylv = 0

    def Hung(self):
        logger.info("запуск голодания")
        while DeadMenager.alive():
            time.sleep(2)
            self.weight -= 1

            if self.weight > 100:
                self.obestylv -= 1

    def Eat(self, item_id):
        logger.info("запуск приёма пищи")
        """Применяет эффект еды по её id."""
        try:
            food_id = int(item_id)

            # Создаем объект еды через фабрику
            edible = EdibleFactory.create_edible('food')

            # Получаем характеристики еды по её id
            food_item = next((item for item in edible.getfoodlist() if item['id'] == food_id), None)

            if food_item['col'] == 0:
                print("Еда отсутствует")
                return

            self.weight += food_item['points']
            self.happy.happylv += food_item['points']

            if self.weight > 100:
                self.Obesty()

            # Уменьшаем количество еды
            food_item['col'] -= 1
            logger.info(f"успешный приём пищи, текущие состояние еды: {self.weight} счастья: {self.happy.happylv}")
            # Вывод информации
            print(f"\nВы покормили {self.name}"
                  f"\nВес: {self.weight}"
                  f"\nОжирение: {self.obestylv}"
                  f"\nРадость: {self.happy.happylv}")



        except ValueError:
            print('Неправильное значение')
            self.Eat()

    def Obesty(self):
        self.obestylv = self.weight - 100

    def DeadFood(self):
        while DeadMenager.alive():
            if self.weight == 0:
                self.health.healthlv = 0