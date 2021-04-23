class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def show_speed(self):
        print(f"скорость {self.name} равна {self.speed}")

class TownCar(Car):
    def show_speed(self):
        return "превышение скорости" if self.speed > 60 else f"скорость {self.name} {self.speed} per hours"

class WorkCar(Car):
    def show_speed(self):
        return "превышение скорости" if self.speed > 40 else f"скорость {self.name} {self.speed} per hours"

ford = TownCar('focus','black',90,1)
print(ford.go())
infinity = WorkCar('mango','black',30,1)
print(infinity.show_speed())






