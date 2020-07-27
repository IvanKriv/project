class Worker:
    incomes = {'Оклад': 42000,
               'Премия': 15000}
    name = 'Сергей'
    surname = 'Зодченко'
    position = 'Менеджер'
    _income = incomes['Оклад']
class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}.')
    def get_total_income(self):
        print(f'Доход сотрудника с учётом премии: {self._income + self.incomes["Премия"]}')

pos = Position()
pos.get_full_name()
pos.get_total_income()
