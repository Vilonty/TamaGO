from src.items.edible import Edible
from src.log.logger_config import logger

#Статический метод еды
class Food(Edible):
    #Изменил с массива на словарь
    foodlist = [
        {"id": 1, "name": "Картошка", "points": 5, "quantity": 2, "col": 2, "type": "food","img":"food.png"},
        {"id": 2, "name": "Морковка", "points": 6, "quantity": 3, "col": 2, "type": "food","img":"food.png"},
        {"id": 3, "name": "Пицца", "points": 8, "quantity": 4, "col": 2, "type": "food","img":"food.png"},
        {"id": 4, "name": "Печенье", "points": 10, "quantity": 5, "col": 2, "type": "food","img":"food.png"},
        {"id": 5, "name": "Торт", "points": 12, "quantity": 10, "col": 2, "type": "food","img":"food.png"},
    ]

    #Статический метод добавления еды
    @staticmethod
    def setPoints(num, pnum):
        logger.info("запуск приёма пищи")
        #Создание массива key, содержащую название ключей и pnum который
        #будет вытаскивать название нужного ключа

        if Food.foodlist[num-1]["col"] == 0:
            return 0

        key = ["name","points","quantity"][pnum]
        #Возврат параметров еды
        return Food.foodlist[num - 1][key]

    @staticmethod
    def getfoodlist():

        return Food.foodlist