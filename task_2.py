with open('file_task_2.txt', 'r', encoding='utf-8') as f_obj:
    string_list = f_obj.readlines()
    f_obj.seek(0)                                       # Для
    print(f'\t\tСодержимое файла: \n{f_obj.read()}')    # удобства
    print()                                             # понимания
    print(f'В данном файле {len(string_list)} строк(и)')
    for i in range(len(string_list)):
        string = string_list[i].split()
        print(f'В строке {i + 1} {len(string)} слов(а)')
