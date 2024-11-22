from dataclasses import dataclass
import json
from pathlib import Path
from typing import TypeVar

from config import JSON_FILE
from db.writers.base import BaseWriter

Data = TypeVar("Data", bound=dict)


@dataclass
class JSONWriter(BaseWriter):
    """Менеджер для записи данных в JSON-файл
    
    :param Path path: Путь к файлу
    """

    path: Path

    def write(self, data: Data):
        """Запись данных в файл

        :param Data data: Данные для записи
        """
        with open(self.path, "w", encoding="UTF-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
