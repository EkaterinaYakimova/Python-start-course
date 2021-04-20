with open("test 2.txt") as my_file:
    content = my_file.read()
    print(f'Количество строк в файле - {len(content)}')
my_file = open("test 2.txt", 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} - ой строки {len(content[i])}')
my_file.close()


