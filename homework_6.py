data_structure = []
product_info = {}
CHOICE = input('Нажмите Enter чтобы добавить товар: ')
n = 1
while CHOICE != '2':
    product_info['название'] = input('Наименование товара: ')
    product_info['цена'] = input('Цена товара: ')
    product_info['количество'] = input('Количество товара: ')
    product_info['ед'] = input('Единица измерения: ')
    product = (n, product_info.copy())
    data_structure.append(product)
    n += 1
    CHOICE = input(
        '''
        Выбирите нужный вариант:
        1 - добавить ещё один товар
        2 - все данные введены
        '''
    )


analytics = {}
names = []
prices = []
quantity = []
mesure = []
for i in range(len(data_structure)):
    names.append(data_structure[i][1]['название'])
    prices.append(data_structure[i][1]['цена'])
    quantity.append(data_structure[i][1]['количество'])
    mesure.append(data_structure[i][1]['ед'])

analytics['название'] = names
analytics['цена'] = prices
analytics['количество'] = quantity
analytics['ед'] = mesure

print(analytics) #не осилил красывый вывод (каждая пара на новой строке)