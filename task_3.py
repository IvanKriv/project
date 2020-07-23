from functools import reduce
def summ(prev_num, num):
    return prev_num + num

with open('file_task_3.txt', 'r', encoding='utf-8') as f_obj:
    staff_list = f_obj.readlines()
    incomes = []
    for i in range(len(staff_list)):
        staff_list[i] = staff_list[i].split()
        incomes.append(staff_list[i][1])
        if '\n' in staff_list[i][1]:
            staff_list[i][1] = staff_list[i][1][:len(staff_list[i][1]) - 2]
        if float(staff_list[i][1]) > 20000:
            print(f'Больше 20000 зарабатывает {staff_list[i][0]}')
    for i in range(len(incomes)):
        incomes[i] = float(incomes[i])
    print(f'Средняя величина дохода сотрудников: {reduce(summ, incomes) / len(incomes)}')


