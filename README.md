<h2 align="center">В данном проекте представленна реализация 3-x версий CRUD приложения(ветка-v1, ветка-v2, ветка-v3) </h2>

<pre>
            1 - версия это реализация с использованием библиотеки fast api но без отделения бизнес логики
            2-  в этой версии  отделена бизнес логика и структурированы файлы в проекте
            <b style="color: red">3 - версия это версия по условию задачи которая написана в файле Task.md </b>

</pre>

# Консольное приложение для управления библиотекой книг

## Описание

Это консольное приложение позволяет управлять библиотекой книг. Оно поддерживает следующие операции:

1. Добавление книги: Пользователь вводит название, автора и год издания книги, после чего книга добавляется в библиотеку с уникальным ID и статусом "в наличии".

2. Удаление книги: Пользователь вводит ID книги, которую нужно удалить.

3. Поиск книги: Пользователь может искать книги по названию, автору или году издания.

4. Отображение всех книг: Приложение выводит список всех книг с их ID, названием, автором, годом издания и статусом.

5. Изменение статуса книги: Пользователь вводит ID книги и новый статус ("в наличии" или "выдана").

## Требования

- Python 3.x

## Установка и запуск

1. Клонируйте репозиторий или скопируйте файл library.py.
2. Запустите приложение с помощью команды:

   `bash
   python library.py

## Функционал

### Добавление книги
```python
def add_book(title: str, author: str, year: int):
    """Добавляет новую книгу в библиотеку."""

```

### Удаление книги
```python
def delete_book(book_id: int):
    """Удаляет книгу по ID."""

```

### Поиск книги
```python
def search_books(query:str):
    """Ищет книги по запросу."""

```
### Отображение всех книг
```
def display_books(books: List[Dict[str, Union[int, str]]]):
    """Отображает список книг."""

```

### Изменение статуса книги
```python
def change_status(book_id: int, new_status:str):
    """Изменяет статус книги."""

```

### Обработка ошибок
<pre>Приложение обрабатывает следующие ошибки:
  Попытка удаления несуществующей книги.
  Неверный ввод данных пользователем.</pre>
### Дополнительные возможности
<pre><i>Аннотации:</i> Функции и переменные аннотированы для лучшей читаемости и поддержки.
<i>Документация:</i> Функции и основные блоки кода снабжены документацией.
<i>Объектно-ориентированный подход:</i> Используется класс Book для представления книги.</pre>
### Тестирование
<pre>Для тестирования можно использовать следующие сценарии:
Добавление нескольких книг.
Поиск книг по различным критериям.
Изменение статуса книги.
Удаление книги.
Попытка удаления несуществующей книги.</pre>
### Автор
 <i>Евгений Савельев</i> <br>
 резюме <a>https://maikop.hh.ru/applicant/resumes/view?resume=d4b31c67ff0e06c5660039ed1f64706e787943


### Заключение

Этот проект демонстрирует базовые CRUD операции для управления библиотекой книг с использованием 
консольного интерфейса. Он также включает в себя обработку ошибок, аннотации, 
документацию и объектно-ориентированный подход.

### Пример работы приложения

![Снимок экрана 2024-11-25 в 18 36 35](https://github.com/user-attachments/assets/6479cb47-9c7c-455e-8175-131082d4dad9)

