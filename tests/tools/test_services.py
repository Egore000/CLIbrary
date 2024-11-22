from unittest import TestCase

import config
from db.readers.readers import JSONReader
from db.writers.writers import JSONWriter
from domain.entities.books import Book
from domain.values.books import Author, Status, Title, Year
from repo.books import Library
from tools import services
from tools.exceptions.commands import InvalidSearchModeException
from tools.services import input_value, input_book_data, find_books
from db import init


table = [
    (Title, "", "a" * 500, "Title"),
    (Author, "", 103, "Author"),
    (Year, 5000, "", "year", "5000", 2000),
    (Status, 12, "", "status", "Выдана", "В наличии"),
]


class SimulatedInput:

    def __init__(self, *args):
        self.args = iter(args)

    def __call__(self, x):
        try:
            return next(self.args)
        except StopIteration:
            raise StopIteration


class TestServices(TestCase):

    def setUp(self):
        self.JSON_FILE = config.JSON_FILE
        config.JSON_FILE = config.BASE_DIR / "data" / "test_library.json"
        init.library = init.LibraryService(
            Library(), 
            JSONWriter(config.JSON_FILE), 
            JSONReader(config.JSON_FILE)
        )
        return super().setUp()

    def test_input_value(self):
        for VT, *_, value in table:
            with self.subTest(f"{VT.__name__}: {value}"):
                services.input = lambda msg: value

                result = input_value(VT)

                self.assertIsInstance(result, VT)
                self.assertEqual(result.value, value)

    def test_input_book_data(self):
        services.input = SimulatedInput("Title", "Author", 2001, "Выдана") 

        book = input_book_data()

        self.assertIsInstance(book, Book)

        self.assertIsInstance(book.title, Title)        
        self.assertEqual(book.title.value, "Title")        

        self.assertIsInstance(book.author, Author)        
        self.assertEqual(book.author.value, "Author")

        self.assertIsInstance(book.year, Year)        
        self.assertEqual(book.year.value, 2001)

        self.assertIsInstance(book.status, Status)        
        self.assertEqual(book.status.value, "Выдана")

    def test_find_book_correct_data(self):
        cases = [
            ("1", "ecee3364-3546-4035-b3ff-054ff7077c3c"),
            ("2", "Преступление и наказание"),
            ("3", "Ф.М. Достоевский"),
            ("4", 1865),
        ]

        for mode, value in cases:
            with self.subTest(f"Mode: {mode}, value: {value}"):
                services.input = SimulatedInput(mode, value)

                books = find_books()
                self.assertIsInstance(books, list) 

                book = books[0]
                self.assertEqual(book.id, "ecee3364-3546-4035-b3ff-054ff7077c3c")
                self.assertEqual(book.title.value, "Преступление и наказание")
                self.assertEqual(book.author.value, "Ф.М. Достоевский")
                self.assertEqual(book.year.value, 1865)

    def test_find_book_incorrect_data(self):
        cases = [
            ("5", ""),
            (1, ""),
            ("аааа", "ааа"),    
        ]

        for mode, value in cases:
            with self.subTest(f"Mode: {mode}, value: {value}"):
                with self.assertRaises(InvalidSearchModeException):
                    services.input = SimulatedInput(mode, value)
                    book = find_books()
                
    def tearDown(self):
        services.input = input
        config.JSON_FILE = self.JSON_FILE
        init.library = init.LibraryService(
            Library(), 
            JSONWriter(self.JSON_FILE), 
            JSONReader(self.JSON_FILE)
        )
        return super().tearDown()
    