from unittest import TestCase

from domain.entities.books import Book
from domain.values.books import Author, Status, StatusValue, Title, Year
from repo.books import Library


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
            status=Status("В наличии")
        )
        self.book_id = self.book.id
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
    
    
    

        