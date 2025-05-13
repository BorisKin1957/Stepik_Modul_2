'''Примите от пользователя две строки с предложениями.
И выведите количество общих слов в этих предложениях'''

import sys

result = set()

for line in sys.stdin:
    st = set(line.strip().split())
    if result:
        result &= st
    else:
        result |= st

print(len(result))
