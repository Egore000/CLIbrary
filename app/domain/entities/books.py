from dataclasses import dataclass, field
from uuid import uuid4 

from domain.values.books import Title, Author, Year, Status


@dataclass
class Book:
    """Модель данных для книги"""
    
    id = field(
        default_factory=lambda: str(uuid4()),
        kw_only=True
    )
    title: Title
    author: Author
    year: Year
    status: Status

