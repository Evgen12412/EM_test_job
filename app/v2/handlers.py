from fastapi import APIRouter, status, HTTPException

from app.v2 import schemas
from app_v2.core import exeptions, update, delete
from app_v2.core import search
from app_v2.core.create import create
from app_v2.storage.storage import books

router = APIRouter()

@router.get(
    '/books/',
    status_code=status.HTTP_200_OK,
    response_model=schemas.BookListResponse,
)
async def get_books():
    '''возвращает список книг '''
    items = search.books()
    return {'items': items}

@router.get(
    '/book/{book_id}/',
    status_code=status.HTTP_200_OK,
    response_model=schemas.BookResponse
)
async def get_book(book_id: int):
    '''возвращает книгу по id '''
    try:
        book = search.book(book_id)
    except exeptions.ItemNotFound:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post(
    '/book/',
    status_code=status.HTTP_200_OK,
    response_model=schemas.BookCreateResponse
)
async def create_book(request: schemas.BookCreateRequest):
    '''добавить книгу '''
    book = create(request.title, request.author, request.year, request.status)
    return {'id': book['id']}


@router.put(
    '/book/{book_id}/',
    status_code=status.HTTP_200_OK,
    response_model=schemas.BookUpdateResponse
)
async def update_book(book_id: int, request: schemas.BookUpdateRequest):
    '''изменить данные по книге '''
    try:
        update.book(book_id, request.model_dump(exclude_none=True))
    except exeptions.ItemNotFound:
        raise HTTPException(status_code=404, detail="Book not found")
    return {'id': book_id}


@router.delete(
    '/book/{book_id}/',
    status_code=status.HTTP_200_OK,
    response_model=schemas.BookDeleteResponse
)
async def delete_book(book_id: int):
    '''удалить книгу'''
    try:
        delete.book(book_id)
    except exeptions.ItemNotFound:
        raise HTTPException(status_code=404, detail="Book not found")
    return {'id': book_id}