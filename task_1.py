import time as t
class TrafficLight:
    __colour = None
    def running(self):
        self.__colour = 'Red'
        print(self.__colour)
        t.sleep(7)
        self.__colour = 'Yellow'
        print(self.__colour)
        t.sleep(2)
        self.__colour = 'Green'
        print(self.__colour)
        t.sleep(5)
        self.__colour = 'Yellow'
        print(self.__colour)
        t.sleep(2)
        self.__colour = 'Red'
        print(self.__colour)
tl = TrafficLight()
tl.running()

