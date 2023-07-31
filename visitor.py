import abc

from typing import List

class IVisitor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def visit(self, place: 'IPlace'):
        pass

class IPlace(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def accept(self, visitor: IVisitor):
        pass

class Zoo(IPlace):
    def accept(self, visitor: IVisitor):
        visitor.visit(self)

class Cinema(IPlace):
    def accept(self, visitor: IVisitor):
        visitor.visit(self)

class Circus(IPlace):
    def accept(self, visitor: IVisitor):
        visitor.visit(self)

class HolidayMaker(IVisitor):
    def __init__(self):
        self.value = ''

    def visit(self, place: 'IPlace'):
        if isinstance(place, Zoo):
            self.value = 'Слоны в зоопарке'
        elif isinstance(place, Cinema):
            self.value = 'Фильм - Властелин колец и власть огня'
        elif isinstance(place, Circus):
            self.value = 'Клоуны в цирке'

if __name__ == '__main__':
    places : List[IPlace] = [Zoo(), Cinema(), Circus()]

    for place in places:
        visitor = HolidayMaker()
        place.accept(visitor)
        print(visitor.value)