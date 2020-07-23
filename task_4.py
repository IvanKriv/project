TRANSLATE = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
with open('file_task_4.txt', 'r', encoding='utf-8') as f_obj:
    string_list = f_obj.readlines()
    for i in string_list:
        i = i.split(' - ')
        with open('task_4_translate.txt', 'a', encoding='utf-8') as trans_f:
            print(TRANSLATE[i[0]], '-', i[1], end='', file=trans_f)
