from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar

from db.readers.base import BaseReader
from db.writers.base import BaseWriter
from domain.entities.base import Entity


T = TypeVar("T", bound=Entity)


@dataclass
class BaseRepository(ABC):

    @abstractmethod
    def add(self, item: T):
        ...

    @abstractmethod
    def get(self, **kwargs) -> T:
        ...

    @abstractmethod
    def get_all(self) -> list[T]:
        ...

    @abstractmethod
    def delete(self, id: str):
        ...

