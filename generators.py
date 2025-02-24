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
    Генератор для генерации номеров банковских карт в формате XXXX XXXX XXXX XXXX.

    Принимает диапазон значений и генерирует номера карт в этом диапазоне, форматируя их в виде:
    "XXXX XXXX XXXX XXXX".

    :param start: Начальное значение диапазона для генерации номеров карт (например, 1).
    :param end: Конечное значение диапазона для генерации номеров карт (например, 5).
    :return: Итератор, который поочередно возвращает номера карт в формате "XXXX XXXX XXXX XXXX".
    """
    for num in range(start, end + 1):
        # Форматирование номера карты в виде XXXX XXXX XXXX XXXX
        yield f"{num:016d}"[:4] + " " + f"{num:016d}"[4:8] + " " + f"{num:016d}"[8:12] + " " + f"{num:016d}"[12:16]
