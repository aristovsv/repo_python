file = open("text_1.txt", "w")
file.write(" sky\n sea\n sun\n")
file.close()
file = open("text_1.txt", "r")

for i in file:
    print(i)

file.close()