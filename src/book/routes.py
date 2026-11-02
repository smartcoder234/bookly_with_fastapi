from fastapi import APIRouter, HTTPException, status
from src.book.book_data import books
from src.book.schema import CreateBookSchema, BookListResponse, BookUpdateSchema, BookResponseSchema
from uuid import uuid4
from datetime import datetime

book_router = APIRouter()

@book_router.get('/books', status_code=status.HTTP_200_OK, response_model=BookListResponse )
def get_books():
    return {
        'message': f'{len(books)} total book(s) found',
        "books": books
    }

@book_router.post('/books', status_code=status.HTTP_201_CREATED)
def create_book(book:CreateBookSchema):
    book_data = book.model_dump()
    new_book = {
        "id": uuid4(),
        "title": book_data['title'],
        "author": book_data['author'],
        "publisher": book_data['publisher'],
        "published_date": book_data['published_date'],
        "page_count": book_data['page_count'],
        "language": book_data['language'],
        'created_at': datetime.today()
    }

    books.append(new_book)

    # return {"message": "Book Added successfully", "user": new_book}
    return new_book

@book_router.get('/books/{book_id}', response_model=BookResponseSchema, status_code=status.HTTP_200_OK)
def get_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Book not found'
    )

@book_router.patch('/books/{book_id}')
def get_book(book_id, book:BookUpdateSchema):
    book_data = book.model_dump(exclude_unset=True,exclude_none=True)
    for book in books:
        if book["id"] == book_id:
            book["title"] =  book_data.get('title', book['title'])
            book["author"] = book_data.get('author', book['author'])
            book["publisher"] = book_data.get('publisher', book['publisher'])
            book["published_date"] = book_data.get('published_date', book['published_date'])
            book["page_count"] = book_data.get('page_count', book['page_count'])
            book["language"] = book_data.get('language', book['language'])

            return book
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Book not found'
    )

@book_router.delete("/book/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)

            return {}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")