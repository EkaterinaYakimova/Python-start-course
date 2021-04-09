a = input('Введите строку разделенную пробелами - ')
items = a.split()
for i, item in enumerate(items, 1):
    print(f'{i} {item[:10]}')

