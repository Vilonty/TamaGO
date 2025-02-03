from src.items.edible import Edible

class Food(Edible):
    foodlist = [
        {"name": "Еда 1", "points": 5, "quantity": 2},
        {"name": "Еда 2", "points": 6, "quantity": 2},
        {"name": "Еда 3", "points": 10, "quantity": 2}
    ]

    @staticmethod
    def setPoints(num, pnum):

        key = ["name","points","quantity"][pnum]
        return Food.foodlist[num - 1][key]