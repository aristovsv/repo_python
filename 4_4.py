from random import randint

list = [randint(0, 20) for i in range(10)]
# проверка
# list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [number for number in list if list.count(number) == 1]
print(list)
print(result)
