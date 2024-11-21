from abc import ABC, abstractmethod
from pathlib import Path
from typing import TypeVar


Data = TypeVar("Data", bound=dict)


class BaseReader(ABC):

    @abstractmethod
    def read(self, path: Path) -> Data:
        ...
