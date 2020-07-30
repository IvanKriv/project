from abc import ABC, abstractmethod


class Cloth(ABC):
    def __init__(self, size, height):
        self.size = size
        self.height = height

    @abstractmethod
    def calculation(self):
        pass

class Coat(Cloth):
    @property
    def calculation(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Cloth):
    @property
    def calculation(self):
        return round(2 * self.height + 0.3, 2)



coat = Coat(42, 184)
suit = Suit(42, 184)
print(f'На пальто необходимо {coat.calculation} кв.м ткани')
print(f'На пальто необходимо {suit.calculation} кв.м ткани')
print(f'Суммарно необходимо {coat.calculation + suit.calculation} кв.м. ткани')
# Числа странные, но вроде бы всё по формулам
