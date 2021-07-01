class Stationery:
    def __init__(self, title="канцтовар"):
        self.title = title

    def draw(self):
        print ("запуск отрисовки")
        print(">" * 40)


class Pen(Stationery):
    def draw(self):
        print("тонкая синяя линия -", self.title)


class Pencil(Stationery):
    def draw(self):
        print("простая черта -",self.title)


class Marker(Stationery):
    def draw(self):
        print("красное подчеркивание -",self.title)


item = Stationery()
item.draw()
pen = Pen("Ручка гелевая")
pen.draw()
pencil = Pencil("Обычный карандаш")
pencil.draw()
marker = Marker("Маркер текстовыделитель")
marker.draw()