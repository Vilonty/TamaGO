from src.items.edible import Edible

class Pills(Edible):
    pillslist = [["Таблетка 1", 0],
                 ["Таблетка 2", 5]]

    @staticmethod
    def setPoints(num):
        return Pills.pillslist[num-1][1]