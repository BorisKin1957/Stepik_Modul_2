percent = int(input())
salary = [2000, 1800, 3100, 4400, 1500]

salary_with_bonus = list(map(lambda x: x + x * percent / 100, salary))

print(salary_with_bonus)