from collections import Counter
from typing import Dict, List


def count_categories(transactions: List[Dict[str, str]]) -> Dict[str, int]:
    # Объявляем тип для category_counter как Counter
    category_counter: Counter[str] = Counter()

    for transaction in transactions:
        # Получаем описание транзакции и приводим его к нижнему регистру для унификации
        description = transaction.get("description", "").lower()
        # Увеличиваем счетчик для каждой категории
        category_counter[description] += 1

    return dict(category_counter)
