rating = [7, 5, 3, 3, 2]
new_elem = int(input('Введите новый элемент рейтинга: '))
#организовать перебор
#пока число меньше или равно рассматриваемому, переходить к следующему эл-ту
#если число больше рассматриваемого, записать его на эту позицию.
for i in range(len(rating)):
    if new_elem > rating[i]:
        rating.insert(i, new_elem)
        break
    else:
        rating.append(new_elem)
        break
print(rating)