from dataclasses import dataclass

from db.readers.base import BaseReader
from db.readers.readers import JSONReader
from db.writers.base import BaseWriter
from db.writers.writers import JSONWriter
from domain.entities.books import Book
from domain.values.books import Author, Status, Title, Year
from repo.base import BaseRepository
from repo.books import Library


@dataclass
class LibraryService:
    """
    Вспомогатальный сервис для работы с данными через репозиторий

    :param BaseRepository library: Репозиторий для работы с данными
    :param BaseWriter writer: Менеджер записи в хранилище
    :param BaseReader reader: Менеджер чтения из хранилища
    """

    library: BaseRepository
    writer: BaseWriter
    reader: BaseReader

    def __post_init__(self):
        self.library.books = self.deserialize()

    def add(self, book: Book):
        """Добавление книги в хранилище

        :param Book book: Книга
        """
        self.library.add(book)
        self.save()

    def get(
        self,
        *,
        id: str = None,
        title: Title = None,
        author: Author = None,
        year: Year = None,
        status: Status = None,
    ) -> Book:
        """Получение книги по заданным параметрам

        :param str id: ID книги
        :param Title title: Название книги
        :param Author author: Автор книги
        :param Year year: Год издания книги
        :param Status status: Статус книги

        :return: Искомая книга
        :rtype: Book
        """
        return self.library.get(
            id=id, title=title, author=author, year=year, status=status
        )

    def filter(
        self,
        *,
        id: str = None,
        title: Title = None,
        author: Author = None,
        year: Year = None,
        status: Status = None,
    ) -> list[Book]:
        """Получение списка книг по заданным параметрам

        :param str id: ID книги
        :param Title title: Название книги
        :param Author author: Автор книги
        :param Year year: Год издания книги
        :param Status status: Статус книги

        :return: Искомые книги
        :rtype: list[Book]
        """
        return self.library.filter(
            id=id, title=title, author=author, year=year, status=status
        )

    def get_all(self) -> list[Book]:
        """Вывод всех книг из БД

        :return: Список книг
        :rtype: list[Book]
        """
        return self.library.get_all()

    def delete(self, id: str):
        """Удаление книги из БД по ID

        :param str id: ID книги
        """
        self.library.delete(id=id)
        self.save()

    def change_status(self, id: str, status: Status):
        """Изменение статуса книги

        :param str id: ID книги
        :param Status status: Статус книги
        """
        self.library.change_status(id, status)
        self.save()

    def save(self):
        """Сохранение данных в БД"""
        books = self.library.serialize()
        self.writer.write(books)

    def deserialize(self):
        """Десериализатор, преобразующий JSON в словарь

        :return: Словарь БД
        :rtype: dict[str, Book]
        """
        return {
            book["id"]: Book(
                id=book["id"],
                title=Title(book["title"]),
                author=Author(book["author"]),
                year=Year(book["year"]),
                status=Status(book["status"]),
            )
            for book in self.reader.read()
        }

    def exists(self, id: str) -> bool:
        """Проверка наличия объекта с id в БД
        
        :param str id: ID книги

        :return: Существует ли объект с данным ID в хранилише
        :rtype: bool
        """

        return self.library.exists(id)


library = LibraryService(Library(), JSONWriter(), JSONReader())
