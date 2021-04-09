my_list = [7, 5, 3, 3, 2]
while True:
    new_number = int(input('Введите новое число-'))
    i = 0
    for item in my_list:
        if new_number <= item:
            i += 1
    my_list.insert(i, int(new_number))
    print(my_list)
