'''Вам даны координаты точек:

points = [
(12, 55),
(880, 123),
(64, 64),
(190, 1024),
(77, 33),
(42, 11),
(0, 90)
]
Вам нужно написать программу, которая берет от пользователя координаты точки и
выводит наиболее близкую точку из приведенных выше к точке, которую задал пользователь.

Формула для нахождения расстояния между точками:

'''

def get_distances_between_points(coord_1: tuple, coord_2: tuple) -> float:
    '''Функция для нахождения расстояния между точками'''
    return round((((coord_1[0] - coord_2[0]) ** 2) + ((coord_1[1] - coord_2[1]) ** 2)) ** 0.5, 2)


points = [
(12, 55),
(880, 123),
(64, 64),
(190, 1024),
(77, 33),
(42, 11),
(0, 90)
]

data = tuple(map(int, input().split()))

distances = [get_distances_between_points(tpl, data) for tpl in points]

index = distances.index(min(distances))

print(*points[index])