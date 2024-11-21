import json
import os
from pathlib import Path
from typing import TypeVar

from config import JSON_FILE
from db.readers.base import BaseReader


Data = TypeVar("Data", bound=dict)


class JSONReader(BaseReader):
    """Менеджер для чтения данных из JSON-файла"""

    def read(self, path: Path = JSON_FILE) -> Data:
        """Чтение данных из файла
        
        :param Path path: Путь к файлу

        :return: Данные
        """
        if os.path.exists(path):
            with open(path, "r", encoding="UTF-8") as file:
                return json.load(file)
        else:
            return {}