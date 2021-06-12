profit = int(input("введите показатель прибыли: "))
cost = int(input("введите показатель издержек: "))
pers = int(input("сколько человек работает в фирме: "))

if profit > cost:
    print ("компания показала прибыль")
    revenue = profit / cost * 100
    print ("рентабельность составила ", int(revenue), "%")
    rev_pers = revenue / pers
    rev_pers = int (rev_pers)
    print("прибыль на одного человека составила ", rev_pers)
elif profit == cost:
    print("вы закрылись в ноль, чем будете платить зарплату", pers, "сотрудникам?")
else:
    print ("компания показала убыток")
