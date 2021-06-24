from itertools import count, cycle

n = int(input("введите n: "))
number = count(1)
letter = cycle("qwerty")

for i in range(n):
    print(next(number), next(letter))