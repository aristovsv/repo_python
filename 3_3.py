def my_func (a=int(input("введите первое число: ")), b=int(input("введите второе число: ")),\
             c=int(input("введите третье число: "))):
    list = [a, b, c]
    list.remove(min(list))
    print("два макисимальных числа ",list)
    return sum(list)
print(my_func())