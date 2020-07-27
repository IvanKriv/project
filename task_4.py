class Car:
    is_police = False
    def __init__(self, speed, colour, name):
        self.speed = speed
        self.colour = colour
        self.name = name
    def go(self):
        print(f'Машина заведена и начала движение.')
    def stop(self):
        print('Машина остановилась, двигатель заглушен.')
    def turn(self, direction):
        print(f'Едим {direction}')
    def show_speed(self):
        print(f'Машина {self.name} едит со скоростью {self.speed}')
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Машина {self.name} едит более 60км/ч! Это превышение, нужно сбавить ход.')
class SportCar(Car):
    pass    # Не совсем понял, что делать с классами где не нужно ничего переопределять...
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Машина {self.name} едит более 40км/ч! Это превышение, нужно сбавить ход.')
class PoliceCar(Car):
    is_police = True

tc = TownCar(62, 'Black', 'Opel')
print('Машина класса TownCar:')
tc.go()
tc.stop()
tc.turn('направо')
tc.turn('налево')
tc.show_speed()
print(tc.name)
print(tc.colour)
sc = SportCar(172, 'Red', 'Porshe')
print('Машина класса SportCar:')
sc.go()
sc.stop()
sc.show_speed()
print(sc.name)
print(sc.colour)
print('Машина класса WorkCar:')
wc = WorkCar(45, 'White', 'Ford')
wc.show_speed()
print(wc.name)
print(wc.colour)
print('Машина класса PoliceCar:')
pc = PoliceCar(90, 'Blue', 'Chevrolet')
pc.show_speed()
print(pc.name)
print(pc.colour)
