my_list = [7, 5, 3, 3, 2]
add_num = int(input('Введите число'))

if add_num > my_list[0]:
    my_list.insert(0, add_num)
else:
    for i, value in enumerate(my_list):
        if value == add_num:
            my_list.insert(i, add_num)
            break
        elif value > add_num:
            continue
        elif value < add_num:
            my_list.insert(i, add_num)
            break
    else:
        my_list.append(add_num)

print(my_list)
