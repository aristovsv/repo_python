def office():
    wages = {}
    with open('taxt_3.txt', 'r', encoding='utf-8') as file:
        for line in file:
            wages[line.split()[0]] = float(line.split()[1])
        print("оклад менее 20000 руб")
        print("-" * 30)
        for name, wage in wages.items():
            if wage < 20000:
                print(name, " - оклад", wage, "руб")
        print("-" *45)
        print(f'Средняя зарплата равна {sum(wages.values()) / len(wages)} руб')

office()
