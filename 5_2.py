file = open("text_2.txt", "w", encoding="utf-8")
file.write(" Питер Москва Казань\n Астрахань Тула Вологда Архангельск\n Омск Красноярск\n")
file.close()

file = open("text_2.txt", encoding="utf-8")
line = 0

for i in file:
    line += 1
    word = 0
    var = 0
    for j in i:
        if j != ' ' and var == 0:
            word += 1
            var = 1
        elif j == ' ':
            var = 0

    print(i, word, "слова")
print("всего", line, "строки")

file.close()


