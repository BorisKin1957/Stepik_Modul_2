''' Напишите программу, которая берет от пользователя начальное число насекомых
в первый день и выводит сколько будет в течении следующих 12 месяцев'''

n = int(input())

print([n * (2 ** i) for i in range(12)])