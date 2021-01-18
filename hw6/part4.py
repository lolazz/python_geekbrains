class Car:
    def __init__(self, speed, name, isPolice):
        self.speed = speed
        self.name = name
        self.isPolice = isPolice

    def go(self):
        print("car is going")

    def stop(self):
        print("car is stopping")

    def turn(self, direction):
        print("car is turning " + direction)

    def show_speed(self):
        print(f'"you are going {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'"you are going over 60!!: {self.speed}')
        else:
            print(self.speed)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'"you are going over 40!!: {self.speed}')
        else:
            print(self.speed)


class PoliceCar(Car):
    def __init__(self):
        Car.__init__(self, 100, "police", True)


work_car = WorkCar(70, "wk", False)
work_car.show_speed()
work_car.speed = 40
work_car.show_speed()
print(work_car.isPolice)

police = PoliceCar()

police.show_speed()
print(police.isPolice)
