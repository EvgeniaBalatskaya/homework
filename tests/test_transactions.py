from typing import Dict, List

from src.transactions import count_categories


def test_count_categories() -> None:
    transactions = [
        {"description": "Payment for services"},
        {"description": "Payment for services"},
        {"description": "Refund for services"},
    ]

    result = count_categories(transactions)

    assert result == {"payment for services": 2, "refund for services": 1}


def test_empty_transactions() -> None:
    transactions: List[Dict[str, str]] = []
    result = count_categories(transactions)

    assert result == {}


def test_invalid_data() -> None:
    transactions = [
        {"description": "Payment for services"},
        {"description": "Refund for services"},
        {"description": "Invalid operation"},
    ]

    result = count_categories(transactions)

    assert result == {"payment for services": 1, "refund for services": 1, "invalid operation": 1}
