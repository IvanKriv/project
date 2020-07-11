user_string = input('Введите строку из нескольких слов: ')
user_string = user_string.split()
for i, word in enumerate(user_string):
    if len(word) <= 10:
        print(f'{i + 1}) {word}')
    else:
        print(f'{i + 1}) {word[:10]}')