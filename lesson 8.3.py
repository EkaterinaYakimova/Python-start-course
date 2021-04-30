class NotNumber(ValueError):
    def __init__(self, my_list):
        self.my_list = []

my_list = []

while True:
    try:
        value = input('Введите число ')
        if value == 'stop':
            break
        if not value.isdigit():
            raise NotNumber(value)
        my_list.append(int(value))
    except NotNumber as ex:
        print('Вы ввели строку', ex)
print(my_list)


