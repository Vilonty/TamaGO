from src.items.edible import Edible

class Food(Edible):
    foodlist = [["Еда 1", 5, 2], ["Еда 2", 6, 2], ["Еда 3", 10, 2]]

    @staticmethod
    def setPoints(num, pnum):
        return Food.foodlist[num - 1][pnum]