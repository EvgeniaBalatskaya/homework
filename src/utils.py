import json
from typing import List, Dict

def read_json_file(file_path: str) -> List[Dict]:
    """
    Читает JSON-файл с транзакциями и возвращает список словарей.
    Если файл пустой, не содержит список или отсутствует — возвращает пустой список.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return []
