def summa():
        with open('file 5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел: ')
            file_obj.writelines(line)
            my_numb = line.split()
            return sum(map(int, my_numb))
print(summa())

