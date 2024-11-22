from unittest import TestCase

from config import TITLE_MAX_LENGTH
from domain.exceptions.books import (
    EmptyTextException,
    InvalidStatusException,
    InvalidYearException,
    TitleTooLongException,
)
from domain.values.books import Author, Status, Text, Title, Year


class TestYearValue(TestCase):

    def test_create_success_int_value(self):
        year = Year(2013)
        self.assertEqual(year.value, 2013)

    def test_create_success_str_value(self):
        year = Year("2013")
        self.assertEqual(year.value, 2013)

    def test_create_big_int_value(self):
        with self.assertRaises(InvalidYearException):
            year = Year(10000)

    def test_create_empty_value(self):
        with self.assertRaises(InvalidYearException):
            year = Year("")

    def test_as_generic_type_int_value(self):
        year = Year(2012)
        self.assertIsInstance(year.as_generic_type(), int)

    def test_as_generic_type_str_value(self):
        year = Year("2012")
        self.assertIsInstance(year.as_generic_type(), int)


class TestText(TestCase):

    def test_create_text(self):
        text = Text("Some text")

        self.assertEqual(text.value, "Some text")

    def test_create_empty_text(self):
        with self.assertRaises(EmptyTextException):
            text = Text("")

    def test_as_generic_type(self):
        text = Text("Text")
        self.assertIsInstance(text.value, str)


class TestTitle(TestCase):

    def test_create_title(self):
        title = Title("Some title")

        self.assertEqual(title.value, "Some title")

    def test_create_empty_title(self):
        with self.assertRaises(EmptyTextException):
            title = Title("")

    def test_create_long_title(self):
        with self.assertRaises(TitleTooLongException):
            Title("a" * (TITLE_MAX_LENGTH + 1))

    def test_as_generic_type(self):
        title = Title("Title")
        self.assertIsInstance(title.value, str)


class TestStatus(TestCase):

    def test_create_status_AVAILABLE(self):
        status = Status("В наличии")
        self.assertEqual(status.value, "В наличии")

    def test_create_status_GIVEN(self):
        status = Status("Выдана")
        self.assertEqual(status.value, "Выдана")

    def test_create_incorrect_status(self):
        with self.assertRaises(InvalidStatusException):
            Status("Статус")

    def test_as_generic_type(self):
        status = Status("В наличии")
        self.assertIsInstance(status.value, str)
