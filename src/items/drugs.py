from src.items.edible import Edible
from src.log.logger_config import logger
#Статический метод еды
class Drug(Edible):
    #Изменил с массива на словарь
    drugs = [
        {"id": 200,"name": "Наркотик 1", "quantity": 20, "col": 2, "type": "drug","img":"drug.png"},
        {"id": 201,"name": "Наркотик 2", "quantity": 30, "col": 2, "type": "drug","img":"drug.png"},
        {"id": 202, "name": "Наркотик 3", "quantity": 30, "col": 2, "type": "drug", "img": "drug.png"},
        {"id": 203, "name": "Наркотик 4", "quantity": 30, "col": 2, "type": "drug", "img": "drug.png"},
    ]

    #Статический метод добавления еды
    @staticmethod
    def setPoints(num):

        #Создание массива key, содержащую название ключей и pnum который
        #будет вытаскивать название нужного ключа
        logger.info("запуск приёма наркотиков")
        if Drug.drugs[num-1]["col"] == 0:
            return 0

        #Возврат параметров еды
        return Drug.drugs[num - 1]["quantity"]

    @staticmethod
    def getdrugslist():

        return Drug.drugs