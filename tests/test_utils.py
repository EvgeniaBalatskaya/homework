import json

from typing import Dict, List


def read_json(file_path: str) -> List[Dict]:
    """
    Читает данные из JSON-файла и возвращает список транзакций.

    :param file_path: Путь к файлу JSON.
    :return: Список транзакций в формате словарей.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
