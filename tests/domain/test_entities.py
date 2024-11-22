from unittest import TestCase

from domain.entities.books import Book
from domain.values.books import Author, Status, StatusValue, Title, Year


class TestBook(TestCase):

    def test_create_book(self):
        title = Title("Title")
        author = Author("Author")
        year = Year(2000)
        status = Status(StatusValue.available)

        book = Book(title=title, author=author, year=year, status=status)

        self.assertEqual(book.title, title)
        self.assertEqual(book.author, author)
        self.assertEqual(book.year, year)
        self.assertEqual(book.status, status)
        self.assertIsInstance(book.id, str)
