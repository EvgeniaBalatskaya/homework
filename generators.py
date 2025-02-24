from typing import Dict, Iterator, List


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Генератор для фильтрации транзакций по валюте.

    Принимает список транзакций и возвращает итератор, который выдает только те транзакции,
    где валюта операции соответствует заданной.

    :param transactions: Список транзакций, каждая транзакция представлена как словарь.
    :param currency: Валюта, по которой производится фильтрация (например, "USD").
    :return: Итератор, который поочередно возвращает транзакции с указанной валютой.
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор для получения описаний транзакций.

    Принимает список транзакций и возвращает итератор, который поочередно выдает описание каждой транзакции.

    :param transactions: Список транзакций, каждая транзакция представлена как словарь.
    :return: Итератор, который поочередно возвращает описание каждой транзакции.
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генерирует номера карт в заданном диапазоне.
    """
    for num in range(start, end):  # ← Здесь `stop` уже НЕ включается
        yield f"{num:04d} {num % 10000:04d} {num % 10000:04d} {num % 10000:04d}"
