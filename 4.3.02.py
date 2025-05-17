def get_shortest_word(word1: str, word2: str) -> str:
    '''
    возвращает короткое слово
    '''
    return min((word1, word2), key=len)


print(get_shortest_word(input(), input()))