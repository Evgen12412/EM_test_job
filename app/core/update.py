from app.core import exeptions
from app.storage.storage import books as books_


def book(book_id: int, data: dict):
    for book_ in books_:
        if book_["id"] == book_id:
            book_.update(data)
            return book_
    raise exeptions.ItemNotFound
