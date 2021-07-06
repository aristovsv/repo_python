class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:5}", end="")
            print()
        return ''
    def __add__(self, new):
        for i in range(len(self.my_list)):
            for x in range(len(new.my_list[i])):
                self.my_list[i][x] = self.my_list[i][x] + new.my_list[i][x]
        return Matrix.__str__(self)


m = Matrix([[1, 6, 12], [-1, 2, -3], [10, 0, 0], [15, 9, -7]])
new_m = Matrix([[-2, 0, 0], [1, 0, -1], [-12, -2, -2], [0, -8, -1]])
print(m.__add__(new_m))