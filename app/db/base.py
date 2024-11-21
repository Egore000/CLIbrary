
from dataclasses import dataclass

from db.readers.base import BaseReader
from db.writers.base import BaseWriter
from repo.base import BaseRepository


@dataclass
class Database:
    writer: BaseWriter
    reader: BaseReader
    repo: BaseRepository

    def save(self):
        self.writer().write(self.repo.books)

    def read(self):
        self.repo.books = self.reader().read()

