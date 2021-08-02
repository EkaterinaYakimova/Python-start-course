class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, obj):
        self.sumax = self.x + obj.x
        self.sumay = self.y + obj.y

    def __mul__(self, obj):
        self.multx = self.x * obj.x - self.y * obj.y
        self.multy = self.y * obj.x + self.x * obj.y


x = float(input('Введите число'))
y = float(input("Введите число"))
a = ComplexNumber(x, y)
x = float(input("Введите число"))
y = float(input("Введите число"))
b = ComplexNumber(x, y)
a + b
a * b
print('Сложение комплекснх чисел:   %.2f+%.2fj' % (a.sumax, a.sumay))
print('Умножение комплексных чисел: %.2f+%.2fj' % (a.multx, a.multy))