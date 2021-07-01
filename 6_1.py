from time import sleep

class TrafficLight:
    __color = "цвет"

    def running(self):
        while True:
            print("горит красный")
            sleep(7)
            print("горит желтый")
            sleep(2)
            print("горит зеленый")
            sleep(7)
            print("горит желтый")
            sleep(2)


a = TrafficLight()
a.running()
