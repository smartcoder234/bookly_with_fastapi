from fastapi import FastAPI
from src.book.routes import book_router
from src.users.routes import user_router

version = 'v1'

app = FastAPI(title='Bookly', description='A RESTful API for a book review web service', version=version)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=['books'])