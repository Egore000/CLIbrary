from dataclasses import dataclass
import json
import os
from pathlib import Path
from typing import TypeVar

from db.readers.base import BaseReader

Data = TypeVar("Data", bound=dict)


@dataclass
class JSONReader(BaseReader):
    """Менеджер для чтения данных из JSON-файла
    
    :param Path path: Путь к файлу для чтения
    """

    path: Path

    def read(self) -> Data:
        """Чтение данных из файла

        :return: Данные
        """
        if os.path.exists(self.path):
            with open(self.path, "r", encoding="UTF-8") as file:
                return json.load(file)
        else:
            return {}
