def factorial(i):
    x = 1
    for i in range(1, n + 1):
        x *= i
        yield x

n = int (input("Укажите число"))
for el in factorial (n):
    print(el)

#  вариант из лекции
from itertools import count
from math import factorial

def fact_gen():
    for el in count(1):
        yield factorial(el)

generator = fact_gen()

x = 0
for i in generator:
    if x == 7:
        break
    else:
        x += 1
        print(f"Factorial {x} = {i}")