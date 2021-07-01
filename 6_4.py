class Car:
    def __init__(self, name, color, speed, is_polis=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_polis
        print("машина:", self.name, "цвет", self.color, "машина полицейская: ", self.is_police)

    def go(self):
        print(self.name, "поехал")

    def stop(self):
        print(self.name, "стоп")

    def turn(self, direction):
        print(self.name, "повернул", ("налево" if direction == 0 else "направо"))

    def show_speed(self):
        print(self.name, "скорость", self.speed)

class TownCar(Car):

    def show_speed(self):
        print(self.name, "Превышение скорости!" if self.speed > 60 else self.name, "Скорость автомобиля", self.speed)


class WorkCar(Car):

    def show_speed(self):
        print(self.name, "Превышение скорости!" if self.speed > 60 else self.name, "Скорость автомобиля", self.speed)


class SportCar(Car):
    ''' Спортивный автомобиль '''

class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


town_car = TownCar("Alfa Romeo", "Красный", 50)
town_car.go()
town_car.turn(1)
town_car.turn(0)
print(town_car.show_speed())
town_car.stop()
print("*" * 40)

work_car = WorkCar("Man", "Желтый", 40)
work_car.go()
work_car.turn(1)
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()
print("*" * 40)

sport_car = SportCar("Lada седан", "Баклажан", 100)
sport_car.go()
sport_car.turn(1)
print(sport_car.show_speed())
sport_car.stop()
print("*" * 40)

police_car = PoliceCar("Ford", "Белый", 80)
police_car.go()
print(police_car.show_speed())
police_car.turn(1)
police_car.stop()
