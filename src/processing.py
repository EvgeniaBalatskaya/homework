# Логика обработки данных (фильтрация, сортировка)
from typing import List, Dict

def filter_by_state(data: List[Dict[str, str]], state: str = "EXECUTED") -> List[Dict[str, str]]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    """
    return [entry for entry in data if entry.get("state") == state]


def sort_by_date(data: List[Dict[str, str]], reverse: bool = True) -> List[Dict[str, str]]:
    """
    Сортирует список словарей по дате в формате ISO.
    """
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
