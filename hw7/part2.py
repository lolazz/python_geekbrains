from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, value):
        self.value = value

    @property
    def consumption(self):
        pass


class Coat(Clothes):
    def consumption(self):
        return self.value / 6.5 + 0.5


class Suite(Clothes):
    def consumption(self):
        return 2 * self.value + 0.3


coat_size = 56
suite_height = 170

coat = Coat(coat_size)
print(f'I\'ll need {coat.consumption()} of material for the coat of size {coat_size}')

suite = Suite(suite_height)
print(f'I\'ll need {suite.consumption()} of material for the coat of height {suite_height}')
