import abc

class Edible(abc.ABC):
    @abc.abstractmethod
    def setPoints(self, *args): pass
