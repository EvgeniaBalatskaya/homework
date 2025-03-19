from typing import Dict, List

import pytest

from src.transactions import count_transactions_by_category, filter_transactions_by_description


@pytest.fixture
def sample_transactions() -> List[Dict[str, str]]:
    return [
        {"id": "1", "description": "Payment for services", "amount": "1000"},
        {"id": "2", "description": "Refund for payment", "amount": "500"},
        {"id": "3", "description": "Payment for goods", "amount": "1500"},
        {"id": "4", "description": "Payment for services", "amount": "2000"},
    ]


def test_filter_transactions_by_description(sample_transactions: List[Dict[str, str]]) -> None:
    # Тестируем фильтрацию транзакций по строке в описании
    result = filter_transactions_by_description(sample_transactions, "Payment for services")
    assert result == [
        {"id": "1", "description": "Payment for services", "amount": "1000"},
        {"id": "4", "description": "Payment for services", "amount": "2000"},
    ]


def test_filter_transactions_by_description_no_match(sample_transactions: List[Dict[str, str]]) -> None:
    # Тестируем, что будет, если нет совпадений
    result = filter_transactions_by_description(sample_transactions, "Nonexistent description")
    assert result == []


def test_count_transactions_by_category(sample_transactions: List[Dict[str, str]]) -> None:
    # Тестируем подсчет транзакций по категориям в описаниях
    categories = ["services", "goods"]
    result = count_transactions_by_category(sample_transactions, categories)
    assert result == {"services": 2, "goods": 1}  # 2 транзакции с "services"  # 1 транзакция с "goods"


def test_count_transactions_by_category_empty(sample_transactions: List[Dict[str, str]]) -> None:
    # Тестируем, что происходит, если категории не найдены
    categories = ["nonexistent"]
    result = count_transactions_by_category(sample_transactions, categories)
    assert result == {"nonexistent": 0}  # Должно быть 0 для всех категорий, которых нет в описаниях


def test_count_transactions_by_category_case_insensitive(sample_transactions: List[Dict[str, str]]) -> None:
    # Тестируем чувствительность к регистру
    categories = ["SERVICES", "goods"]
    result = count_transactions_by_category(sample_transactions, categories)
    assert result == {"SERVICES": 2, "goods": 1}  # Проверка на регистронезависимость


if __name__ == "__main__":
    pytest.main()
