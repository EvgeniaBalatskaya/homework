import json

from pathlib import Path


def read_json(file_path: str) -> list:
    """
    Читает JSON-файл и возвращает список транзакций.
    Если файл пустой, отсутствует или содержит некорректные данные, возвращает пустой список.
    """
    path = Path(file_path)
    if not path.exists():
        return []

    try:
        with path.open(encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, FileNotFoundError):
        return []
