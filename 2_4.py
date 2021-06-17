words = input("введите несколько разных слов через пробелы: ").split()
for number, word in enumerate(words, 1):
    print(number, word) if len(word) <= 10 else print(number, (word[:10]))
