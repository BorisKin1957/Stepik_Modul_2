'''Записать положительные элементы списка X = [x1,x2,...xn]подряд в список
Y=[y1,y2,...yn]. Определить k (количество положительных элементов).
Вычислить сумму элементов списка X и произведение элементов списка Y.

Выведите:

элементы списка Y в строке,
количество элементов в списке Y
сумму элементов списка X
произведение элементов списка '''


def get_multiplication(numbers: list[int]) -> int:
    '''Возвращает произведение чисел списка.'''
    result = 1
    for number in numbers:
        result *= number
    return result

numbers = list(map(int, input().split()))

positives = [num for num in numbers if num > 0]

print(*positives)
print(len(positives), sum(numbers), get_multiplication(positives), sep='\n')
