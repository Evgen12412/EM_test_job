import json
import os
from typing import List, Dict, Union

# Константы
BOOKS_FILE = 'library.json'


class Book:
    def __init__(self, title: str, author: str, year: int, status: str = "в наличии", book_id: int = None):
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        self.book_id = book_id if book_id else self._generate_id()

    def _generate_id(self) -> int:
        """Генерирует уникальный ID для книги."""
        books = load_books()
        if books:
            return max(book['id'] for book in books) + 1
        return 1

    def to_dict(self) -> Dict[str, Union[int, str]]:
        """Преобразует объект Book в словарь."""
        return {
            'id': self.book_id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }


def load_books() -> List[Dict[str, Union[int, str]]]:
    """Загружает книги из файла."""
    if not os.path.exists(BOOKS_FILE):
        return []
    with open(BOOKS_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_books(books: List[Dict[str, Union[int, str]]]):
    """Сохраняет книги в файл."""
    with open(BOOKS_FILE, 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


def add_book(title: str, author: str, year: int):
    """Добавляет новую книгу в библиотеку."""
    books = load_books()
    new_book = Book(title, author, year).to_dict()
    books.append(new_book)
    save_books(books)
    print(f"Книга '{title}' добавлена.")


def delete_book(book_id: int):
    """Удаляет книгу по ID."""
    books = load_books()
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            save_books(books)
            print(f"Книга с ID {book_id} удалена.")
            return
    print(f"Книга с ID {book_id} не найдена.")


def search_books(query: str) -> List[Dict[str, Union[int, str]]]:
    """Ищет книги по запросу (title, author, year)."""
    books = load_books()
    results = []
    for book in books:
        if (query.lower() in book['title'].lower() or
                query.lower() in book['author'].lower() or
                query == str(book['year'])):
            results.append(book)
    return results


def display_books(books: List[Dict[str, Union[int, str]]]):
    """Отображает список книг."""
    if not books:
        print("Книги не найдены.")
        return
    for book in books:
        print(
            f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}")


def change_status(book_id: int, new_status: str):
    """Изменяет статус книги."""
    books = load_books()
    for book in books:
        if book['id'] == book_id:
            book['status'] = new_status
            save_books(books)
            print(f"Статус книги с ID {book_id} изменен на '{new_status}'.")
            return
    print(f"Книга с ID {book_id} не найдена.")


def main():
    """Основная функция для взаимодействия с пользователем."""
    while True:
        print("\nМеню:")
        print("1. Добавить книгу        2. Удалить книгу          3. Поиск книги")
        print("4. Отобразить все книги  5. Изменить статус книги  6. Выход")
        print()

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания: "))
            add_book(title, author, year)

        elif choice == '2':
            book_id = int(input("Введите ID книги для удаления: "))
            delete_book(book_id)

        elif choice == '3':

            query = input("Введите запрос для поиска (название, автор или год): ")
            results = search_books(query)
            display_books(results)

        elif choice == '4':
            books = load_books()
            display_books(books)

        elif choice == '5':
            book_id = int(input("Введите ID книги для изменения статуса: "))
            new_status = input("Введите новый статус (в наличии/выдана): ")
            change_status(book_id, new_status)

        elif choice == '6':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
