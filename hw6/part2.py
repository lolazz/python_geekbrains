class Road():
    def __init__(self, leght, width):
        self.__lengh = leght
        self.__width = width

    def calculate_weight(self, weight, thickness):
        return self.__width * self.__lengh * weight * thickness


road = Road(20, 5000)
print(road.calculate_weight(25, 5))
