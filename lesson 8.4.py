class Sklad:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class Equipment:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year
        self.group = self.__class__.__name__


    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.make} {self.year}'


class Printer(Equipment):
    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series

    def __repr__(self):
        return f'{self.name} {self.series} {self.make} {self.year}'

    def action(self):
        return 'Печатает'


class Scaner(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Сканирует'


class Xerox(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Копирует'


sklad = Sklad()
# создаем объект и добавляем
scaner = Scaner('hp', '321', 90)
sklad.add_to(scaner)
scaner = Scaner('Canon', 5, 10)
sklad.add_to(scaner)
scaner = Scaner('hp', '330', 99)
sklad.add_to(scaner)
printer = Printer('hp', 200, 10, 2017)
sklad.add_to(printer)
# выводим склад
print(sklad._dict)
# забираем с склада и выводим склад
sklad.extract('Scaner')
print()
print(sklad._dict)