a = int(input('сколько км пробежал спортсме в первый день: '))
b = int(input('сколько км нужно пробежать спортсмену: '))
day = 1
while a < b:
    a = a + a * 0.1
    day = day + 1
print("спортсмену потребуется ", day, "дней")
