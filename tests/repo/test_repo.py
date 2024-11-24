from unittest import TestCase

from domain.entities.books import Book
from domain.values.books import Author, Status, Title, Year
from repo.books import Library
from repo.exceptions.books import ObjectNotFoundException


class TestLibraryRepo(TestCase):

    def setUp(self):
        self.library = Library()

        self.title = Title("Title")
        self.author = Author("Author")
        self.year = Year(1995)
        self.status = Status("В наличии")

        self.values = (self.title, self.author, self.year, self.status)

        self.book = Book(
            title=Title("Title"),
            author=Author("Author"),
            year=Year(1995),
            status=Status("В наличии"),
        )
        self.book_id = self.book.id

        self.books = [
            Book(
                Title(f"Book 1"),
                Author(f"Author 1"),
                Year(2000),
                Status("В наличии"),
            ),
            Book(
                Title(f"Book 2"),
                Author(f"Author 1"),
                Year(2010),
                Status("Выдана"),
            ),
            Book(
                Title(f"Book 3"),
                Author(f"Author 2"),
                Year(2000),
                Status("В наличии"),
            ),
            Book(
                Title(f"Book 4"),
                Author(f"Author 2"),
                Year(2000),
                Status("Выдана"),
            ),
        ]
        return super().setUp()

    def test_add_book(self):
        self.assertEqual(self.library.books, dict())

        self.library.add(self.book)

        self.assertNotEqual(self.library.books, dict())
        self.assertIn(self.book_id, self.library.books)
        self.assertEqual(self.library.books.get(self.book_id), self.book)

    def test_get_book(self):
        self.library.add(self.book)
        self.assertNotEqual(self.library.books, dict())

        for value in self.values:
            with self.subTest(f"Searching value: {value}"):
                book = self.library.get(id=self.book_id)
                self.assertEqual(book, self.book)
                self.assertIsInstance(book, Book)

    def test_get_non_existing_book(self):
        with self.assertRaises(ObjectNotFoundException):
            book = self.library.get(id="id")

    def test_get_all_books(self):
        self._add_books()

        books = self.library.get_all()
        self.assertIsInstance(books, list)
        self.assertListEqual(books, self.books)
        self.assertIsInstance(books[0], Book)

    def test_get_all_books_empty_library(self):
        self.assertEqual(self.library.books, dict())

        books = self.library.get_all()
        self.assertIsInstance(books, list)
        self.assertListEqual(books, [])

    def test_delete_book(self):
        self.assertEqual(self.library.books, dict())
        self.library.add(self.book)

        self.library.delete(self.book_id)
        self.assertEqual(self.library.books, dict())

    def test_delete_non_existing_book(self):
        self.assertEqual(self.library.books, dict())
        self.library.add(self.book)

        with self.assertRaises(ObjectNotFoundException):
            self.library.delete(id="id")

    def test_change_status(self):
        self.library.add(self.book)

        status = self.book.status
        new_status = Status("Выдана")

        self.library.change_status(id=self.book_id, status=new_status)

        self.assertNotEqual(status, self.book.status)
        self.assertEqual(new_status, self.book.status)

    def test_filter_book_by_id(self):
        self._add_books()

        books = self.library.filter(id=self.books[0].id)

        self.assertIsInstance(books, list)
        self.assertEqual(books[0], self.books[0])

    def test_filter_book_by_title(self):
        self._add_books()

        title = self.books[0].title
        books = self.library.filter(title=title)

        self.assertIsInstance(books, list)
        self.assertEqual(books[0], self.books[0])

    def test_filter_book_by_author(self):
        self._add_books()

        author = self.books[0].author
        books = self.library.filter(author=author)

        self.assertIsInstance(books, list)
        self.assertEqual(books, [book for book in self.books if book.author == author])
        self.assertEqual(len(books), 2)

    def test_filter_book_by_year(self):
        self._add_books()

        year = self.books[0].year
        books = self.library.filter(year=year)

        self.assertIsInstance(books, list)
        self.assertEqual(books, [book for book in self.books if book.year == year])
        self.assertEqual(len(books), 3)

    def test_filter_book_by_status(self):
        self._add_books()

        status = self.books[0].status
        books = self.library.filter(status=status)

        self.assertIsInstance(books, list)
        self.assertEqual(books, [book for book in self.books if book.status == status])
        self.assertEqual(len(books), 2)

    def test_exists_existing_book(self):
        self._add_book()
        self.assertIn(self.book_id, self.library.books)
        self.assertTrue(self.library.exists(id=self.book_id))

    def test_exists_non_existing_book(self):
        self.assertEqual(self.library.books, dict())
        self.assertNotIn(self.book_id, self.library.books)
        self.assertFalse(self.library.exists(id=self.book_id))

    def _add_books(self):
        for book in self.books:
            self.library.add(book)
        self.assertEqual(list(self.library.books.values()), self.books)

    def _add_book(self):
        self.assertEqual(self.library.books, dict())
        self.library.add(self.book)
        self.assertNotEqual(self.library.books, dict())
