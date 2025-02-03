from src.items.edible import Edible

class Pills(Edible):
    pillslist = [
        {"name": "Таблетка 1", "points": 0},
        {"name": "Таблетка 2", "points": 5}
    ]

    @staticmethod
    def setPoints(num):
        return Pills.pillslist[num-1]["points"]