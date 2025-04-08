from src.items.edible import Edible
from src.log.logger_config import logger
#Статический метод таблеток
class Pills(Edible):
    #Заменил массив на словарь
    pillslist = [
        {"id": 6,"name": "Таблетка 1", "points": 0, "col": 2, "type": "pills","img":"food.png"},
        {"id": 7,"name": "Таблетка 2", "points": 5, "col": 2, "type": "pills","img":"food.png"},
        {"id": 8,"name": "Таблетка 3", "points": 10, "col": 2, "type": "pills","img":"food.png"}
    ]


    #Статический метод получения таблеток
    @staticmethod
    def setPoints(num):
        logger.info("запуск приёма таблеток")
        if Pills.pillslist[num-1]["col"] == 0:
            return 0
        #Возвращение параметров таблетки
        return Pills.pillslist[num-1]["points"]

    @staticmethod
    def getpillslist():

        return Pills.pillslist