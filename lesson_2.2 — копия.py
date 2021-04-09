a = input('Введите несколько элементов  через пробел - ')
a = a.split()
j = 0
for i in range(int(len(a) / 2)):
    a[j], a[j + 1] = a[j + 1], a[j]
    j += 2
print(a)



