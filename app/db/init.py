from db.base import Database
from db.readers.readers import JSONReader
from db.writers.writers import JSONWriter

from repo.books import Library


db = Database(JSONWriter, JSONReader, Library)