import time
class TrafficLight:

    def running(self):
        while True:
            self.__colour = "red"
            print(self.__colour)
            time.sleep(7)
            self.__colour = "yellow"
            print(self.__colour)
            time.sleep(3)
            self.__colour = "green"
            print(self.__colour)
            time.sleep(3)


traffic_light = TrafficLight()
traffic_light.running()