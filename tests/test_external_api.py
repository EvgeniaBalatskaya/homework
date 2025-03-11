from unittest.mock import patch

from src.external_api import convert_to_rub  # Импортируем функцию конвертации


def test_convert_to_rub_valid() -> None:
    """
    Тест для проверки корректной конвертации валюты в рубли.
    """
    transaction = {"amount": 100.0, "currency": "USD"}  # Тестовая транзакция
    # Мокаем функцию получения курса
    with patch("src.external_api.get_exchange_rate", return_value=75.0):
        result = convert_to_rub(transaction)
    assert result == 7500.0  # Ожидаем, что 100 USD * 75 = 7500 RUB
