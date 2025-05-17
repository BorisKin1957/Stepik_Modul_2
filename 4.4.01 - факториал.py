def get_factorial(number: int, factorial_dict={0: 1, 1: 1}) -> int:
    """Рекурсивная функция нахождения факториала числа """
    if number not in factorial_dict:
        factorial_dict[number] = number * get_factorial(number - 1, factorial_dict)
    return factorial_dict[number]


print(get_factorial(int(input())))