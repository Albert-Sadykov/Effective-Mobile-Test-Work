class Book:
    def __init__(self, book_id, title, author, year, status="в наличии"):

        # Инициализация экземпляра класса Book

        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __repr__(self):

        # Возвращает строковое представление объекта Book

        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Year: {self.year}, Status: {self.status}"
