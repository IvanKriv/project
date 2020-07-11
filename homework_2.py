user_list = []
elem_num = int(input('Сколько элементов будет в вашем списке? '))
for i in range(elem_num):
    user_elem = input(f'Введите элемент под индексом {i}: ')
    user_list.append(user_elem)

for k in range(1, elem_num, 2):
    user_list[k], user_list[k - 1] = user_list[k - 1], user_list[k]

print(user_list)