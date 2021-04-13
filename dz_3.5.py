str = input('Введите что-то через пробел- ').split()
def sum_numb(numStr):
    int_lst = (int(x) for x in numStr)
    return sum(int_lst)
print(sum_numb(str))
while True:
    a = sum_numb(str)
    def cal():
        try:
            new_number = int(input('Введите новое число-'))
        except ValueError:
            return 'Нажмите выйти из программы или'
        result = a + new_number
        return result
    result = cal()
    print(result)


