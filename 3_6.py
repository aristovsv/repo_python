def int_func(word):
    latin_chair = "qwertyuiopasdfghjklzxcvbnm"
    return word.title() if not set(word).difference(latin_chair) else False

words = input("введите слова через пробел: ").split()
for i in words:
    result = int_func(i)
    if result:
        print(int_func(i), " ")
