from time import sleep


class Trafficlight:
    __color = 'черный'

    def running (self):
        while True:
            print('Красный')
            sleep(7)
            print("желтый")
            sleep(2)
            print('Зеленый')
            sleep(9)

light = Trafficlight()
light.running()