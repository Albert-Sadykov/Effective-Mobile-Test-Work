from library import Library
from storage import save_to_file, load_from_file

def main():
    
    # Основная функция для запуска программы

    library = load_from_file()
    print("Добро пожаловать в систему управления библиотекой!")

    while True:
        print("\nВыберите действие:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Сохранить и выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            book = library.add_book(title, author, year)
            print(f"Книга добавлена: {book}")

        elif choice == "2":
            book_id = input("Введите ID книги для удаления: ")
            if library.remove_book(book_id):
                print("Книга удалена.")
            else:
                print("Книга не найдена.")

        elif choice == "3":
            title = input("Введите название книги (или оставьте пустым): ")
            author = input("Введите автора книги (или оставьте пустым): ")
            year = input("Введите год издания книги (или оставьте пустым): ")
            results = library.search_books(title, author, year)
            if results:
                for book in results:
                    print(book)
            else:
                print("Книги не найдены.")

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            book_id = input("Введите ID книги для изменения статуса: ")
            status = input("Введите новый статус (в наличии/выдана): ")
            if library.update_status(book_id, status):
                print("Статус книги обновлен.")
            else:
                print("Книга не найдена.")

        elif choice == "6":
            save_to_file(library)
            print("Данные сохранены. Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите действие из списка.")

if __name__ == "__main__":
    main()
