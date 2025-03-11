import json

from pathlib import Path
from typing import Any, List


def read_json(file_path: str) -> List[dict[str, Any]]:
    """
    Читает JSON-файл с банковскими операциями и возвращает список транзакций.

    :param file_path: Путь к JSON-файлу.
    :return: Список словарей с транзакциями.
    """
    file = Path(file_path)

    if not file.exists() or not file.is_file():
        return []

    try:
        with file.open(encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                return []
            return data
    except (json.JSONDecodeError, ValueError):
        return []
