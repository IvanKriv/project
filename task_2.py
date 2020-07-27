class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def asphalt_mass(self):
        one_m_mass = 25
        thickness = int(input('Введите требуемую толщину покрытия в см: '))
        return self._length * self._width * one_m_mass * thickness
r = Road(5000, 20)
print(f'Для покрытия данного участка дороги, требуется {r.asphalt_mass()/1000} тонн асфальта.')
# Подскажите пожалуйста, как можно было бы убрать три нуля с конца, при помощи встроенного форматирования строк?
