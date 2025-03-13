from typing import Dict, List

from src.transactions import count_categories


# Тест для функции count_categories
def test_count_categories() -> None:
    # Тестовые данные
    transactions: List[Dict[str, str]] = [
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод с карты на карту"},
        {"description": "Открытие вклада"},
        {"description": "Перевод организации"},
        {"description": "Перевод с карты на карту"},
    ]

    # Ожидаемый результат
    expected_result: Dict[str, int] = {"перевод с карты на карту": 3, "открытие вклада": 1, "перевод организации": 1}

    # Вызов функции
    result = count_categories(transactions)

    # Проверка на корректность
    assert result == expected_result


def test_empty_transactions() -> None:
    # Пустой список транзакций
    transactions: List[Dict[str, str]] = []

    # Ожидаемый результат - пустой словарь
    expected_result: Dict[str, int] = {}

    result = count_categories(transactions)

    assert result == expected_result


def test_missing_description() -> None:
    # Тест с транзакциями без описания
    transactions: List[Dict[str, str]] = [
        {"description": "Перевод с карты на карту"},
        {"description": ""},
        {"description": "Открытие вклада"},
    ]

    expected_result: Dict[str, int] = {
        "перевод с карты на карту": 1,
        "открытие вклада": 1,
        "": 1,  # Пустая категория тоже должна быть учтена
    }

    result = count_categories(transactions)

    assert result == expected_result
