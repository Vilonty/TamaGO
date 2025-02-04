"""
Статичный класс смерти

Используется во всей программе и заканчивает игру при функции kill

Он обрубает главный процесс, а так как все параллельные процессы - это процессы демоны, то игра заканчивается
"""


class DeadMenager:
    livest = 1

    #Статичный метод смерти
    @staticmethod
    def kill():
        DeadMenager.livest = 0
        exit()

    #Статичный метод жизни
    @staticmethod
    def alive():
        return DeadMenager.livest
