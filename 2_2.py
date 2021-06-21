my_list = []
n = 0
for i in range(7):
    n += 1
    print("введите", n, "число ")
    my_list.append(input(""))

my_list_1 = my_list[0:n:2]
my_list_2 = my_list[1:n:2]

my_list_res = my_list_2[0] + my_list_1[0] + my_list_2[1] + my_list_1[1] + my_list_2[2] + my_list_1[2] + my_list_1[3]

print(list(my_list_res))
