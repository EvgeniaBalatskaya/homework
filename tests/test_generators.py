from typing import Dict, List

from generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions: List[Dict[str, Dict[str, Dict[str, str]]]]) -> None:
    """
    Тестирует функцию filter_by_currency, которая фильтрует транзакции по валюте.
    Ожидаем, что функция вернет только транзакции с валютой USD.
    """
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}},
        {"operationAmount": {"currency": {"code": "USD"}}},
        {"operationAmount": {"currency": {"code": "RUB"}}},
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2, "Должно быть 2 транзакции с валютой USD"
    assert result[0]["operationAmount"]["currency"]["code"] == "USD", "Первая транзакция должна быть с валютой USD"


def test_transaction_descriptions(transactions: List[Dict[str, str]]) -> None:
    """
    Тестирует функцию-генератор transaction_descriptions, которая возвращает описания транзакций.
    Ожидаем, что функция вернет правильные описания транзакций.
    """
    transactions = [{"description": "Перевод организации"}, {"description": "Перевод со счета на счет"}]
    result = list(transaction_descriptions(transactions))
    assert result == ["Перевод организации", "Перевод со счета на счет"], "Описание транзакций не совпадает"


def test_card_number_generator() -> None:
    """
    Тестирует функцию-генератор card_number_generator, которая генерирует номера карт в заданном диапазоне.
    Ожидаем, что функция вернет правильное количество номеров карт в диапазоне от start до stop.
    """
    result = list(card_number_generator(1000000000000000, 1000000000000010))
    assert len(result) == 10, "Должно быть сгенерировано 10 номеров карт"
    assert result[0] == "1000000000000000", "Первый номер карты должен быть 1000000000000000"
