from pydantic import BaseModel
class CreateBookSchema(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    created_at: str|None=None

class BookResponseSchema(BaseModel):
    id: str
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    created_at: str|None=None

class BookListResponse(BaseModel):
    message:str
    books: list[BookResponseSchema]

class BookUpdateSchema(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str