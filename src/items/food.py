from src.items.edible import Edible


#Статический метод еды
class Food(Edible):
    #Изменил с массива на словарь
    foodlist = [
        {"name": "Еда 1", "points": 5, "quantity": 2},
        {"name": "Еда 2", "points": 6, "quantity": 2},
        {"name": "Еда 3", "points": 10, "quantity": 2}
    ]

    #Статический метод добавления еды
    @staticmethod
    def setPoints(num, pnum):

        #Создание массива key, содержащую название ключей и pnum который
        #будет вытаскивать название нужного ключа
        key = ["name","points","quantity"][pnum]

        #Возврат параметров еды
        return Food.foodlist[num - 1][key]