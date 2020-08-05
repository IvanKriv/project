class CheckEl(Exception):
    def __init__(self, text):
        self.text = text

user_input = None
num_list = []
while user_input != 'q':
    user_input = input('Введите новый числовой элемент списка.\n Для выхода введитe "q"')
    try:
        if not user_input.isdigit():
            raise CheckEl('Вводите только числовые значания или "q" для выхода!')
        user_input = int(user_input)
        num_list.append(user_input)
        print(f'На данный момент ваш список таков: {num_list}')
    except CheckEl as ce:
        print(ce)
