import re

from typing import Dict, List


def filter_transactions_by_description(transactions: List[Dict[str, str]], search_string: str) -> List[Dict[str, str]]:
    """
    Фильтрует транзакции по описанию, используя регулярное выражение.

    :param transactions: Список транзакций.
    :param search_string: Строка для поиска в описании.
    :return: Список транзакций, где описание содержит строку поиска.
    """
    pattern = re.compile(search_string, re.IGNORECASE)  # Регулярное выражение с игнорированием регистра
    return [transaction for transaction in transactions if pattern.search(transaction["description"])]


def count_transactions_by_category(transactions: List[Dict[str, str]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по категориям, исходя из поля "description".

    :param transactions: Список транзакций.
    :param categories: Список категорий, по которым нужно посчитать количество операций.
    :return: Словарь, где ключи — категории, а значения — количество операций.
    """
    count_by_category = {category: 0 for category in categories}

    for transaction in transactions:
        description = transaction.get("description", "").lower()  # Приводим описание к нижнему регистру
        for category in categories:
            if category.lower() in description:
                count_by_category[category] += 1

    return count_by_category
