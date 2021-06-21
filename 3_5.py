def sum ():
    i = 0
    while True:
        print("для выхода нажмите *")
        numbers = input("введите несколько чисел через пробел: ").split()
        for number in numbers:
            if number == "*":
                return i
            else:
                number = int(number)
                i += number
        print(i)
print(sum())