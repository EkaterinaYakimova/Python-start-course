from functools import reduce

items = [el for el in range(99, 1001) if el % 2 == 0]
print(items)

print(f'результат вычисления произведения всех элементов списка {reduce(lambda x,y: x*y, items)}')