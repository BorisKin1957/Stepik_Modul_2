def get_sum_sqrt_list(numbers: list[int]) -> int:
    """Нахождение суммы квадратов чисел списка"""
    if not numbers:
        return 0
    return numbers.pop() ** 2 + get_sum_sqrt_list(numbers)


new_list = [int(i) for i in input() if i.isdigit()]

print(get_sum_sqrt_list(new_list))