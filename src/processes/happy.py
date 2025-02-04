from src.mainprocesses.dead import DeadMenager
import time
class Happy:

    def __init__(self):

        self.happylv = 50
        self.happymax = 100

        #face пока не используется
        self.__face = 3

    def sad(self):

        #Грусть
        while DeadMenager.alive():
            time.sleep(5)
            self.happylv -= 1