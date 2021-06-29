dic = {}
numbers = "1234567890 "

with open("text_6.txt", "r", encoding="utf-8") as file:
    for line in file:
        head, hours = line.split(":")
        dic[head] = sum(map(int, "".join([num for num in hours if num in numbers]).split()))
print(dic)