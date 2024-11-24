from dataclasses import dataclass, field

from domain.entities.books import Book
from domain.values.books import Author, Status, Title, Year
from repo.base import BaseRepository
from repo.exceptions.books import ObjectNotFoundException


@dataclass
class Library(BaseRepository):
    """Библиотека, объединяющая в себе методы для работы с книгами

    :param dict[str, Book] books: База данных
    """

    books: dict[str, Book] = field(default_factory=dict, kw_only=True)

    def add(self, book: Book):
        """Добавить книгу

        :param Book book: Книга
        """
        self.books[book.id] = book

    def get(
        self,
        *,
        id: str = None,
        title: Title = None,
        author: Author = None,
        year: Year = None,
        status: Status = None,
    ) -> Book:
        """Поиск книги по заданным параметрам

        :param str id: ID книги
        :param Title title: Название книги
        :param Author author: Автор книги
        :param Year year: Год издания книги
        :param Status status: Статус книги

        :return: Искомая книга
        :rtype: Book

        :raises ObjectNotFoundException: Книга не найдена
        """
        book = self.filter(id=id, title=title, author=author, year=year, status=status)

        if not book:
            raise ObjectNotFoundException
        return book[0]

    def get_all(self) -> list[Book]:
        """Вывод всех книг, хранящихся в БД

        :return: Список книг
        :rtype: list[Book]
        """
        return list(self.books.values())

    def delete(self, id: str):
        """Удаление книги по ID

        :param str id: ID книги

        :raises ObjectNotFoundException: Книга не найдена
        """
        if not self.exists(id):
            raise ObjectNotFoundException
        self.books.pop(id)

    def change_status(self, id: str, status: Status) -> Book:
        """Изменение статуса задачи

        :param str id: ID книги
        :param Status status: Статус книги

        :return: Книга с измененным статусом
        :rtype: Book

        :raises ObjectNotFoundException: Книга не найдена
        """
        book = self.books.get(id)

        if not book:
            raise ObjectNotFoundException
        book.status = status
        return book

    def filter(
        self,
        *,
        id: str = None,
        title: Title = None,
        author: Author = None,
        year: Year = None,
        status: Status = None,
    ) -> list[Book]:
        """Поиск книг по заданным параметрам

        :param str id: ID книги
        :param Title title: Название книги
        :param Author author: Автор книги
        :param Year year: Год издания книги
        :param Status status: Статус книги

        :return: Искомые книга
        :rtype: list[Book]

        :raises ObjectNotFoundException: Книги не найдены
        """

        result: list[Book] = []
        for book in self.books.values():
            if (
                book.id == id
                or book.title == title
                or book.author == author
                or book.year == year
                or book.status == status
            ):

                result.append(book)

        if not result:
            raise ObjectNotFoundException
        return result

    def serialize(self):
        """Сериализатор для представления данных в формате JSON"""
        return [item.as_dict() for item in self.books.values()]

    def exists(self, id: str) -> bool:
        """Проверка наличия объекта с id в БД

        :param str id: ID книги

        :return: Существует ли объект с данным ID в хранилише
        :rtype: bool
        """

        return id in self.books.keys()
