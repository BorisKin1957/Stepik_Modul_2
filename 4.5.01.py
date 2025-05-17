def get_sum_list(numbers: list[int]) -> int:
    """Нахождение суммы списка"""
    if not numbers:
        return 0
    return numbers.pop() + get_sum_list(numbers)


new_list = [int(i) for i in input() if i.isdigit()]

print(get_sum_list(new_list))