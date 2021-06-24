list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [list[pos] for pos in range(1, len(list)) if list[pos] > list[pos - 1]]
print(result)