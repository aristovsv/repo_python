numbers = ['1', '2', '3', '4']

with open("text_5.txt", "w", encoding="utf-8") as file:
    numbers_new = " ".join(list(map(str, numbers)))
    print("числа, записанные в файл: ", numbers_new)
    file.write(numbers_new)

    numbers_new = list(map(int, numbers))
    numbers_sum = sum(numbers_new)

print("сумма чисел в файле: ", numbers_sum)