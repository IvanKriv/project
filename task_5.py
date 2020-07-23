from functools import reduce
def summ(prev_el, el):
    return prev_el + el
with open('file_task_5.txt', 'w+', encoding='utf-8') as f_obj:
    f_obj.write('22 1 35 644 2 4 54 99')
    f_obj.seek(0)
    numbers = f_obj.read().split()
    numbers_copy = numbers[:]
    for i in range(len(numbers_copy)):
        numbers[i] = int(numbers_copy[i])
    print(f'Сумма чисел в файле: {reduce(summ, numbers)}')
    