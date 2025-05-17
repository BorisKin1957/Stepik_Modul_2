def get_min(*args) -> int:
    '''Функция нахождения минимума среди чисел'''
    minimum = None
    for arg in args:
        if minimum is None or arg < minimum:
            minimum = arg
    return minimum

print(get_min(8, 13, 4, 42, 120, 7))

