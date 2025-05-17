'''Напишите функцию, которая для данного списка подсчитывает сумму и
произведение его элементов'''

def get_sum_and_mult(args: list[str]) -> tuple[int]:
    '''
    Возвращает сумму и произведение чисел списка
    '''
    sum, mult = 0, 1
    for arg in args:
        sum += int(arg)
        mult *= int(arg)
    return sum, mult


print(*get_sum_and_mult(input().split()))
