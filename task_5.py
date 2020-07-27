class Stationery:
    title = 'Заголовок'     # Зачем?))
    def draw(self):
        print('Запуск отрисовки...')
class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой.')
class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом.')
class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером.')

st = Stationery()
st.draw()   # Родительский класс
Pen().draw()    # Ручка
Pencil().draw()     # Карандаш
Handle().draw()     # Маркер
