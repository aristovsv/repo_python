my_list = [7, 5, 3, 3, 2]

number = int(input("введите число: "))
i = 0
for n in my_list:
    if number <= n:
        i += 1

my_list.insert(i, number)
print(my_list)
