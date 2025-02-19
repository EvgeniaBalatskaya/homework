# Логика обработки данных (фильтрация, сортировка)
from typing import List, Dict

def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    """
    return [entry for entry in data if entry.get("state") == state]


def sort_by_date(data: List[dict], reverse: bool = True) -> List[dict]:
    """
    Сортирует список словарей по дате в формате ISO.
    """
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
