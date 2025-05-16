'''Дана база данных о продажах некоторого интернет-магазина.
Каждая строка входного файла представляет собой запись вида Покупатель товар
количество, где Покупатель — имя покупателя (строка без пробелов), товар —
название товара (строка без пробелов), количество — количество приобретенных единиц товара.

Создайте словарь, где ключ - это Покупатель и значение тоже является словарем,
где ключи это товары, которые приобрел соответствующий покупатель.
Для каждого покупателя подсчитайте количество приобретенных им единиц каждого
вида товаров. Ключи словаря, должны быть в лексикографическом порядке.

Sample Input:

Ivanov paper 10
Petrov pens 5
Ivanov marker 3
Ivanov paper 7
Petrov envelope 20
Ivanov envelope 5
Sample Output:

{'Ivanov': {'paper': 17, 'marker': 3, 'envelope': 5}, 'Petrov': {'pens': 5, 'envelope': 20}}'''

import sys

lst = []
for line in sys.stdin:
    lst.append(line.strip().split())

sorted(lst, key=lambda x: x[0])
result = {}

for item in lst:
    name, product, count = item
    result[name] = result.get(name, {})
    result[name][product] = result[name].get(product, 0) + int(count)

print(result)