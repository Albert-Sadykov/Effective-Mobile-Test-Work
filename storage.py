import json
from book import Book
from library import Library

# Функция для сохранения изменений в json файл
def save_to_file(library, filename="library_data.json"):
    with open(filename, "w") as file:
        books_data = [book.__dict__ for book in library.books]
        json.dump(books_data, file)

# Функция для получения данных из json файла
def load_from_file(filename="library_data.json"):
    try:
        with open(filename, "r") as file:
            books_data = json.load(file)
            library = Library()
            for book_data in books_data:
                book = Book(**book_data)
                library.books.append(book)
            return library
    except FileNotFoundError:
        return Library()
