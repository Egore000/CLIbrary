from dataclasses import dataclass, field

from domain.entities.books import Book
from domain.values.books import Status
from repo.base import BaseRepository
from repo.exceptions.books import ObjectNotFoundException


@dataclass
class Library(BaseRepository):
    """Библиотека, объединяющая в себе методы для работы с книгами"""

    books: dict[str, Book] = field(default_factory=dict, kw_only=True)

    def add(self, book: Book):
        self.books[book.id] = book

    def get(self, **kwargs) -> Book: 
        book_id = kwargs.pop("id")
        if book_id:
            book = self.books.get(book_id)
        else:
            book = self.filter(**kwargs)
        
        if not book:
            raise ObjectNotFoundException
        return book

    def get_all(self) -> list[Book]:
        result = []
        for item in self.books.values():
            result.append(item.as_dict())
        return result
    
    def delete(self, id: str):
        self.books.pop(id)

    def change_status(self, id: str, status: Status) -> Book:
        book = self.books.get(id)
        book.status = status
        return book
        
    def filter(self, **kwargs) -> Book:
        for book in self.books.values():
            for key, value in kwargs.items():
                if hasattr(book, key):
                    book_value = getattr(book, key)
                    if book_value == value:
                        return book
                    
    def serialize(self):
        return [item.as_dict() for item in self.books.values()]