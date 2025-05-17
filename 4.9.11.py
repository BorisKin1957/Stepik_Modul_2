'''Напишите программу, которая будет запрашивать у пользователя часы и ставку за час.
На основе данных от пользователя рассчитайте заработную плату в неделю.

Зарплата должна вычисляться из условия,

обычная ставка за  часовую нагрузку при работе до 40 часов
полуторную ставка за час  за все часы, отработанные свыше 40 часов.'''


def computepay(hours, rate):
    '''
    Расчет заработной платы с учетом премии за сверхурочную работу
    '''
    if hours <= 40:
        return hours * rate
    else:
        basic_salary = 40 * rate
        extra_salary = (hours - 40) * rate * 1.5
        return basic_salary + extra_salary

hours = int(input())
rate = float(input())
p = computepay(hours, rate)

print("Pay", p)