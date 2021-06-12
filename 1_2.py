time = int(input("Введите любое количество секунд: "))

sec = time % 60
min = (time // 60) % 60
hour = time // 3600

print("чч:мм:cc")
print(f"{hour:02}:{min:02}:{sec:02}")