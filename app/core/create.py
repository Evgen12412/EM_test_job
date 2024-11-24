from app.storage.storage import books as books_


def create(title, author, year, status):
    _id = len(books_) + 1
    book = {
        'id': _id,
        'title': title,
        'author': author,
        'year': year.strftime('%Y') if year else None,
        'status': status
    }
    books_.append(book)
    return book
