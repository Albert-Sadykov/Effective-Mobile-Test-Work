import uuid
from book import Book

class Library:

    # Класс отвечающий за управление книгами
    
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        book_id = str(uuid.uuid4())
        new_book = Book(book_id, title, author, year)
        self.books.append(new_book)
        return new_book

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                return True
        return False

    def search_books(self, title=None, author=None, year=None):
        results = []
        for book in self.books:
            if (title and title.lower() in book.title.lower()) or \
               (author and author.lower() in book.author.lower()) or \
               (year and year == book.year):
                results.append(book)
        return results

    def display_books(self):
        for book in self.books:
            print(book)

    def update_status(self, book_id, status):
        for book in self.books:
            if book.book_id == book_id:
                book.status = status
                return True
        return False
