import json

from typing import Dict, List


def read_json(file_path: str) -> List[Dict]:
    """
    Читает JSON из файла и возвращает список словарей.
    Если данные не могут быть распарсены или это не список, возвращает пустой список.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # Проверяем, что данные - это список
            if isinstance(data, list):
                return data
            else:
                return []  # Если это не список, возвращаем пустой список
    except (json.JSONDecodeError, FileNotFoundError):
        return []  # Если ошибка при чтении, возвращаем пустой список
