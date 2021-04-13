first = int(input('введите первое число '))
second = int(input('введите второе число '))
def my_func(first, second):
    result = 1/(first**second)
    return result
print(my_func(first, second))