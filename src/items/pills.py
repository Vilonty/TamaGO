from src.items.edible import Edible

#Статический метод таблеток
class Pills(Edible):
    #Заменил массив на словарь
    pillslist = [
        {"name": "Таблетка 1", "points": 0},
        {"name": "Таблетка 2", "points": 5}
    ]


    #Статический метод получения таблеток
    @staticmethod
    def setPoints(num):

        #Возвращение параметров таблетки
        return Pills.pillslist[num-1]["points"]