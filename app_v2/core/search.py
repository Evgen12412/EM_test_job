from app_v2.core import exeptions
from app_v2.storage.storage import books as books_

def books():
    return books_

def book(book_id):
    for book_ in books_:
        if book_["id"] == book_id:
            return book_
    raise exeptions.ItemNotFound