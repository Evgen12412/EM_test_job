from fastapi import APIRouter, status, HTTPException
from app.api.v1 import schemas

router = APIRouter()

books = [
    {
        'id': 1,
        'title': "Граф Монте Кристо",
        'author': "Александр Дюма",
        'year': '1844',
        'status': 'в наличии'
    },
    {
        'id': 2,
        'title': "Три мушкетера",
        'author': "Александр Дюма",
        'year': '1844',
        'status': 'выдана',
    },
]

@router.get(
    '/books/',
    status_code=status.HTTP_200_OK,
    response_model=schemas.BookListResponse,
)
async def get_books():
    '''возвращает список книг '''
    return {'items': books}

@router.get(
    '/book/{book_id}/',
    status_code=status.HTTP_200_OK,
    response_model=schemas.BookResponse
)
async def get_book(book_id: int):
    '''возвращает книгу по id '''
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.post(
    '/book/',
    status_code=status.HTTP_200_OK,
    response_model=schemas.BookCreateResponse
)
async def create_book(request: schemas.BookCreateRequest):
    '''добавить книгу '''
    _id = len(books) + 1
    book = {
        'id': _id,
        'title': request.title,
        'author': request.author,
        'year': request.year.strftime('%Y') if request.year else None,
        'status': request.status
    }
    books.append(book)
    return {'id': _id}


@router.put(
    '/book/{book_id}/',
    status_code=status.HTTP_200_OK,
    response_model=schemas.BookUpdateResponse
)
async def update_book(book_id: int, request: schemas.BookUpdateRequest):
    '''изменить данные по книге '''
    for book in books:
        if book["id"] == book_id:
            book.update(request.model_dump(exclude_none=True))
            return {'id' : book_id}
    raise HTTPException(status_code=404, detail="Book not found")


@router.delete(
    '/book/{book_id}/',
    status_code=status.HTTP_200_OK,
    response_model=schemas.BookDeleteResponse
)
async def delete_book(book_id: int):
    '''удалить книгу'''
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {'id' : book_id}
    raise HTTPException(status_code=404, detail="Book not found")