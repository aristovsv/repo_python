class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def total(self, weight=25, thickness=5):
        weight = int(input("введите массу 1 кв.м.: "))
        thickness = int(input("введите толщину: "))
        a = (self._length * self._width * weight * thickness) / 1000
        return a

street = Road(5000, 20)
print("на", street._length, "метров дороги шириной", street._width, "метров, потребуется", street.total(), "тонн асфальта")