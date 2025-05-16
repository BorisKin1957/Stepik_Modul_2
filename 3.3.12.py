'''Клетки на шахматной доске идентифицируется буквой и цифрой.
Буква определяет положение клетки по горизонтали, а цифра - по вертикали,
как показано на рисунке.

Ваша программа должна запрашивать у пользователя координаты клетки(в формате: b2).
Используя арифметику определите какая это клетка: чёрная или белая.'''

a, b = 'Белая', 'Чёрная'

black_white = {'a': b, 'b': a, 'c': b, 'd': a, 'e': b, 'f': a, 'g': b, 'h': a}
white_black = {'a': a, 'b': b, 'c': a, 'd': b, 'e': a, 'f': b, 'g': a, 'h': b}

chess_board = {1: black_white, 3: black_white, 5: black_white, 7: black_white,
       2: white_black, 4: white_black, 6: white_black, 8: white_black}

field = input()

print(chess_board[int(field[1])][field[0]])