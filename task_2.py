class ZeroDivError(Exception):
    def __init__(self, text):
        self.text = text


while True:
    try:
        a = int(input('Введите делимое'))
        b = int(input('Введите делитель'))
        if b == 0:
            raise ZeroDivError('Делитель не может равняться нулю!')
        else:
            print(a / b)
        break
    except ValueError:
        print('Введите числовые значения!')
    except ZeroDivError as zde:
        print(zde)
