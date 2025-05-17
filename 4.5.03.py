def get_reversed_chars(word: str) -> str:
    '''
    Выводит каждый символ переданной строки в обратном порядке
    '''
    if not word:
        return ''
    print(word[-1])
    return get_reversed_chars(word[:-1])


get_reversed_chars(input())
