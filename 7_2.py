from abc import ABC, abstractmethod


class Сlothes(ABC):


    @property
    @abstractmethod
    def total(self):
        pass

    def __add__(self, other):
        return self.total + other.total


class Coat(Сlothes):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
            self.__size = size

    @property
    def total(self):
        return self.__size / 6.5 + 0.5


class Сostume(Сlothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
            self.__height = height

    @property
    def total(self):
        return 2 * (self.__height / 100) + 0.3


new_coat = Coat(int(input('Введите ваш размер: ')))
print(f'{new_coat.total:.2f} метров ткани нужно на пальто')
new_costume = Сostume(int(input('Введите ваш рост: ')))
print(f'{new_costume.total:.2f} метров ткани нужно на костюм')
print(f'Всего необходимо {new_coat + new_costume:.2f} метров ткани')