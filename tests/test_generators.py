import pytest
from generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency() -> None:
    """Тестируем фильтрацию транзакций по валюте."""
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }
    ]

    filtered = list(filter_by_currency(transactions, "USD"))

    assert len(filtered) == 2  # Проверяем, что осталось 2 транзакции
    assert all(txn["operationAmount"]["currency"]["code"] == "USD" for txn in
               filtered)  # Проверяем, что валюты всех транзакций - USD


def test_transaction_descriptions() -> None:
    """Тестируем генератор описаний транзакций."""
    transactions = [
        {
            "description": "Перевод организации",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            }
        },
        {
            "description": "Перевод со счета на счет",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            }
        }
    ]

    descriptions = list(transaction_descriptions(transactions))

    assert len(descriptions) == 2  # Должно быть 2 описания
    assert "Перевод организации" in descriptions  # Проверка наличия описания


def test_card_number_generator() -> None:
    """Тестируем генератор номеров карт."""
    start = 1000000000000000
    stop = 1000000000000010

    card_numbers = list(card_number_generator(start, stop))

    assert len(card_numbers) == 10  # Генератор должен вернуть 10 номеров карт
    assert all(num.startswith("1000000000000") for num in card_numbers)  # Все номера должны начинаться с этого префикса
