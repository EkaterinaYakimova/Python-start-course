#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def calc():
    try:
        first = float(input("Укажите первое число: "))
        second = float(input("Укажите второе число: "))
    except ValueError:
        return 'ошибка'
    result = first/second
    return result
result = calc()
print(result)