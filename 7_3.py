class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for i in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return f"{self.nums}"

    def __add__(self, other):
        print("всего клеток:")
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print("разность клеток:")


    def __mul__(self, other):
        print("произведение клеток:")
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print("частное клеток:")
        return Cell(self.nums // other.nums)


cell_1 = Cell(int(input("введите количество клеток: ")))
cell_2 = Cell(int(input("введите количество клеток: ")))
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(7))