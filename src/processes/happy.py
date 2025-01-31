from src.mainprocesses.dead import DeadMenager
import time
class Happy:

    def __init__(self):

        self.happylv = 50
        self.happymax = 100
        self.__face = 3

    def sad(self):

        while DeadMenager.alive():
            time.sleep(5)
            self.happylv -= 1