# Логика обработки данных (фильтрация, сортировка)

def filter_by_state(data, state='EXECUTED'):
    """
    Фильтрует список словарей по значению ключа 'state'.
    """
    return [entry for entry in data if entry.get('state') == state]


from typing import List

def sort_by_date(data: List[dict], reverse: bool = True) -> List[dict]:
    """
    Сортирует список словарей по дате в формате ISO.
    """
    return sorted(data, key=lambda x: x['date'], reverse=reverse)
