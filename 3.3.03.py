'''Напишите программу, которая принимает от пользователя натуральное число n и
создает словарь, в котором ключами будут
натуральные числа от 1 до n, а значениями будут эти же числа, возведенные в куб.'''

n = int(input())

print({i: i ** 3 for i in range(1, n + 1)})