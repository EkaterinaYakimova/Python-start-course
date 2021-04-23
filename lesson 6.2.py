class Road:
    def __init__(self,leght,width):
        self._leght = leght
        self._width = width

    def massa(self):
        return self._leght * self._width * 25 * 5

road_1 = Road (800,6)
print(road_1.massa())