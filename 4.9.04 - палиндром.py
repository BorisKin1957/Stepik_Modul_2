word = input().lower()

print('Да' if word == word[::-1] else 'Нет')