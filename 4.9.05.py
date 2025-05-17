'''Напишите функцию common_elements(list1, list2), которая принимает на вход
два списка целых чисел и возвращает список,
состоящий из общих элементов двух исходных списков'''

def common_elements(list1, list2):
    return list(set(list1) & set(list2))

print(*common_elements([int(i) for i in input().split()], [int(i) for i in input().split()]))