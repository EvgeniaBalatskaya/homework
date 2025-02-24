from generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions: list[dict[str, dict[str, str]]]) -> None:
    """
    Тестирует функцию filter_by_currency, проверяя, что она корректно фильтрует
    транзакции по заданной валюте (например, USD).

    Args:
        transactions: Список словарей, представляющих транзакции.

    Returns:
        None
    """
    usd_transactions = filter_by_currency(transactions, "USD")
    assert next(usd_transactions)["operationAmount"]["currency"]["code"] == "USD"


def test_transaction_descriptions(transactions: list[dict]) -> None:
    """
    Тестирует функцию transaction_descriptions, проверяя, что она возвращает
    правильные описания транзакций.

    Args:
        transactions: Список словарей, представляющих транзакции.

    Returns:
        None
    """
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Перевод организации"


def test_card_number_generator() -> None:
    """
    Тестирует генератор card_number_generator, проверяя корректность генерации
    номеров карт в заданном диапазоне.

    Returns:
        None
    """
    gen = card_number_generator(1, 5)
    assert next(gen) == "0000 0000 0000 0001"
    assert next(gen) == "0000 0000 0000 0002"
