'''Возьмите от пользователя два списка и выведете информацию

Количество уникальных элементов каждого списка;
Максимальный элемент каждого списка;
Минимальный элемент каждого списка;
Вывести общие элементы для двух списков'''

numbers1 = list(map(int, input().split()))
numbers2 = list(map(int, input().split()))

print(len(set(numbers1)), len(set(numbers2)), sep='\n')
print(max(numbers1), max(numbers2), sep='\n')
print(min(numbers1), min(numbers2), sep='\n')
print(*set(numbers1) & set(numbers2))
