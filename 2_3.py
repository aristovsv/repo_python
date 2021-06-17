month = int(input("Введите месяц года цифрой: "))
season = {"зима": [12, 1, 2], "весна": [3, 4, 5], "лето": [6, 7, 8], "осень": [9, 10, 11]}
if month in sum(season.values(), []):
    for i in season.items():
        if month in i[1]:
            print(i[0])

