file_eng = open("text_4.txt", "r", encoding="utf-8")
file_rus = open("text_4_1.txt", "w", encoding="utf-8")
translate = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

file_rus.writelines([line.replace(line.split()[0], translate.get(line.split()[0])) for line in file_eng])

file_eng.close()
file_rus.close()


