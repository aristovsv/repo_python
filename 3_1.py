def division():
    try:
        var_1 = int(input("введите первое число: "))
        var_2 = int(input("введите второе число: "))
        return int(var_1 / var_2)
    except ZeroDivisionError:
        print("деление на ноль запрещено")

print(division())
