class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def ToInt(cls):
        try:
            date_to_int = my_date.date
            date_to_int = date_to_int.split('-')
            for i in range(len(date_to_int.copy())):
                date_to_int[i] = int(date_to_int.copy()[i])
            return date_to_int
        except ValueError:
            return 'Дата должна содержать числовые значения!'


    @staticmethod
    def Validation():
        if Date.ToInt()[0] not in range(1, 32):
            print('Введена некорректная дата!')
        elif Date.ToInt()[1] not in range(1, 13):
            print('Введена некорректная дата!')
        else:
            print('Все данные введены верно')


my_date = Date('10-11-1997')
print(my_date.ToInt())
Date.Validation()

