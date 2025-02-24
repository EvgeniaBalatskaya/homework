import pytest
from generators import filter_by_currency, transaction_descriptions, card_number_generator

# Пример данных для тестирования
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"}
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
            "currency": {"name": "USD", "code": "USD"}
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
            "currency": {"name": "RUB", "code": "RUB"}
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    }
]

# Тестирование функции filter_by_currency
def test_filter_by_currency():
    """
    Тестирует функцию filter_by_currency.
    Проверяет, что транзакции фильтруются корректно по валюте.
    """
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 2  # Проверка, что найдено 2 транзакции с валютой USD
    assert usd_transactions[0]["description"] == "Перевод организации"
    assert usd_transactions[1]["description"] == "Перевод со счета на счет"


# Тестирование функции transaction_descriptions
def test_transaction_descriptions():
    """
    Тестирует функцию transaction_descriptions.
    Проверяет, что описания транзакций извлекаются корректно.
    """
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет"
    ]


# Тестирование функции card_number_generator
def test_card_number_generator():
    """
    Тестирует функцию card_number_generator.
    Проверяет, что генератор создает корректные номера карт в заданном диапазоне.
    """
    numbers = list(card_number_generator(1, 5))
    assert numbers == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]

# Параметризированный тест для card_number_generator
@pytest.mark.parametrize("start, end, expected", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (4, 6, ["0000 0000 0000 0004", "0000 0000 0000 0005", "0000 0000 0000 0006"])
])
def test_card_number_generator_param(start, end, expected):
    """
    Параметризированный тест для функции card_number_generator.
    Проверяет корректность генерации номеров карт на разных диапазонах.
    """
    numbers = list(card_number_generator(start, end))
    assert numbers == expected
