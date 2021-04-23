class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('запуск отрисовки')

class Pen(Stationary):
    def draw(self):
        print({self.title}, 'ручка')

class Pencil(Stationary):
    def draw(self):
        print({self.title}, 'карандаш')

class  Handle(Stationary):
    def draw(self):
        print({self.title}, 'маркер')

step = Stationary('возьмите')
print(step.draw())
step2 = Pencil('возьмите')
print(step2.draw())
step3 = Handle('возьмите')
print(step2.draw())

