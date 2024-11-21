from dataclasses import dataclass, field
from uuid import uuid4 

from domain.entities.base import Entity
from domain.values.books import Title, Author, Year, Status


@dataclass
class Book(Entity):
    """Модель данных для книги"""
    
    id: str = field(
        default_factory=lambda: str(uuid4()),
        kw_only=True
    )
    title: Title
    author: Author
    year: Year
    status: Status

