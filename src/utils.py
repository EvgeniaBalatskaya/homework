import json
from pathlib import Path
from typing import Any, List


def read_json(file_path: str) -> List[dict[str, Any]]:
    """
    Читает JSON-файл с банковскими операциями и возвращает список транзакций.

    :param file_path: Путь к JSON-файлу.
    :return: Список словарей с транзакциями или пустой список в случае ошибки.
    """
    file = Path(file_path)

    # Проверяем, существует ли файл и является ли он файлом
    if not file.exists() or not file.is_file():
        return []  # Если файл не существует или не является файлом, возвращаем пустой список

    try:
        with file.open(encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                return []  # Если данные не список, возвращаем пустой список
            return data
    except (json.JSONDecodeError, ValueError):
        return []  # В случае ошибки при чтении или декодировании возвращаем пустой список
