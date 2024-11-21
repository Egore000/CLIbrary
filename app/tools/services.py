from dataclasses import dataclass
from db.readers.base import BaseReader
from db.readers.readers import JSONReader
from db.writers.base import BaseWriter
from db.writers.writers import JSONWriter
from domain.entities.books import Book

from domain.values.books import Status
from repo.books import Library
from tools.inputters.books import AuthorInputter, StatusInputter, TitleInputter, YearInputter 


def greetings():
    print("""
            <<<     CLIbrary    >>>
    
Чтобы начать работу, ознакомься со списком команд:
1) get <BOOK> - найти нужную книгу по названию, автору или году.
2) all - вывести все имеющиeся книги.
3) add - добавить книгу.
4) delete <ID> - удалить книгу по ID.
5) status <ID> <STATUS> - изменить статус книги по ID.
6) help - справка.
7) exit - выход.
""")
    

def input_book_data() -> Book:
    """Ввод параметров книги"""

    title = TitleInputter.input()
    author = AuthorInputter.input()
    year = YearInputter.input()
    status = StatusInputter.input()

    return Book(title=title, author=author, year=year, status=status)


@dataclass
class LibraryService:
    library: Library
    writer: BaseWriter
    reader: BaseReader

    def __post_init__(self):
        self.library.books = self.deserialize()

    def add(self, book: Book):
        self.library.add(book)
        self.save()

    def get(self, **kwargs) -> Book: 
        return self.library.get(**kwargs)
    
    def get_all(self) -> list[Book]:
        return self.library.get_all()
    
    def delete(self, id: str):
        self.library.delete(id=id)
        self.save()

    def change_status(self, id: str, status: Status):
        self.library.change_status(id, status)
        self.save()

    def save(self):
        books = self.library.serialize()
        self.writer.write(books)
    
    def deserialize(self):
        return {book["id"]: Book(**book) for book in self.reader.read()}



library = LibraryService(Library(), JSONWriter(), JSONReader())