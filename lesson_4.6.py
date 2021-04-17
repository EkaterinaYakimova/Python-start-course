#импортируется функция count() из модуля itertools, и создаётся цикл for. В скрипт добавляется условная проверка, разрывающая цикл при превышении итератором значения 10. Иначе выводится текущее значение итератора. Результат начинается со значения 3, так как оно определено в качестве стартового.
from itertools import count

for el in count(3):
    if el > 10:
        break
    else:
        print(el)
#итератор, повторяющий элементы некоторого списка, определенного заранее. Дополнительно реализован счётчик для разрыва цикла.

from itertools import cycle

progr_lang = ["python", "java", "perl", "javascript"]

с = 0
for el in cycle(progr_lang):
    if с > 10:
        break
    print(el)
    с += 1



