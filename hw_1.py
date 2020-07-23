with open('file_task_1.txt', 'w+', encoding='utf-8') as f_obj:
    while True:
        user_input = input('Введите данные для ввода в файл. \nДля завершения ввода просто нажмите Enter. ')
        if user_input != '':
            f_obj.write(user_input + '\n')
        else:
            break
    f_obj.seek(0)           # Для проверки
    print(f_obj.read())     # корректности работы
