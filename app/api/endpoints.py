# Эндпоинты для взаимодействия с приложением

import os

from domain.entities.books import Book
from domain.values.books import Status
from repo.exceptions.books import ObjectNotFoundException
from tools.messages import Message
from tools.services import find_books, input_book_data, library


def add_book() -> Book:
    """Добавление книги"""
    book = input_book_data()
    library.add(book)
    print(Message.added, book.id)
    return book


def get_books() -> list[Book]:
    """Поиск книг по заданным параметрам"""
    book = find_books()
    for item in book:
        print(item.human_readable())
    return book


def get_all_books() -> list[Book]:
    """Вывод всех книг, хранящихся в БД"""
    books = library.get_all()
    for book in books:
        print(book.human_readable())
    return books


def delete_book():
    """Удаление книги"""
    id = input(Message.id)
    library.delete(id)
    print(Message.deleted)


def change_status():
    """Изменение статуса книги"""
    id = input(Message.id)

    if library.exists(id):
        status = Status(input(Message.status))
        library.change_status(id=id, status=status)
    else:
        raise ObjectNotFoundException


def help():
    """Помощь с работой приложения"""
    print(Message.help)


def clear():
    """Очистка командной строки"""
    os.system("cls")
