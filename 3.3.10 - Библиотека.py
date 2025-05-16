'''Напишите код, который использует метод .get() вместо операторов if/else
для вывода «Книга не найдена», если такой книги нет в словаре.
Если книга есть в словаре, то выводил ее жанр.

'''

books = {
    "Life of Pi": "Adventure Fiction",
    "The Three Musketeers": "Historical Adventure",
    "Watchmen": "Comics",
    "Bird Box": "Horror",
    "Harry Potter":"Fantasy Fiction",
    "Good Omens": "Comedy"}

print(books.get(input(), 'Книга не найдена'))