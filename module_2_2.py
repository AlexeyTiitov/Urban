my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    namber = my_list[index]

    if namber < 0:
        break
    elif namber == 0:
        index += 1
        continue
    elif namber > 0:
        print(namber)
    index += 1
