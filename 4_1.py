from sys import argv


def salary():
    work_time, rate, bonus = map(float, argv[1:])
    money = work_time * rate + bonus

    print("количество часов: ", work_time)
    print("почасовая ставка: ", rate)
    print("премия: ", bonus)
    print("зарплата составила: ", money)
    return money

salary()
