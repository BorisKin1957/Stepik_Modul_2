'''Напишите свою функцию my_filter(iterable, function)
аналог стандартной функции filter'''

def my_filter(iterable, function):
    return [item for item in iterable if function(item)]


print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3))  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True