import abc
#Забыл навзвание, но класс шаблон с методом setPoints, который является референсом для еды и таблеток
class Edible(abc.ABC):
    @abc.abstractmethod
    def setPoints(self, *args): pass
