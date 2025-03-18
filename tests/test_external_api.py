import pytest
from unittest.mock import patch
from src.external_api import get_exchange_rate, convert_to_rub


# Мокирование API
@pytest.fixture
def mock_requests_get():
    with patch('requests.get') as mock_get:
        yield mock_get


def test_get_exchange_rate(mock_requests_get):
    # Мокируем ответ от API
    mock_response = {
        "result": "75.5"
    }
    mock_requests_get.return_value.json.return_value = mock_response
    mock_requests_get.return_value.raise_for_status = lambda: None  # Игнорируем ошибку для теста

    # Проверяем корректный результат
    result = get_exchange_rate("USD")
    assert result == 75.5


def test_get_exchange_rate_invalid_currency(mock_requests_get):
    # Проверяем, что ValueError поднимется при неверной валюте
    with pytest.raises(ValueError, match="Unsupported currency: ABC"):
        get_exchange_rate("ABC")


def test_get_exchange_rate_invalid_response(mock_requests_get):
    # Мокируем ошибочный ответ от API
    mock_response = {
        "result": "invalid"
    }
    mock_requests_get.return_value.json.return_value = mock_response
    mock_requests_get.return_value.raise_for_status = lambda: None

    # Проверяем, что поднимется ValueError при некорректном значении результата
    with pytest.raises(ValueError, match="Unable to convert result to float"):
        get_exchange_rate("USD")


# Тест для convert_to_rub
def test_convert_to_rub(mock_requests_get):
    # Мокируем ответ для валюты USD
    mock_response = {
        "result": "75.5"
    }
    mock_requests_get.return_value.json.return_value = mock_response
    mock_requests_get.return_value.raise_for_status = lambda: None

    # Пример транзакции в USD
    transaction = {"amount": 100, "currency": "USD"}

    result = convert_to_rub(transaction)
    assert result == 7550.0


def test_convert_to_rub_already_in_rub():
    # Пример транзакции в RUB
    transaction = {"amount": 100, "currency": "RUB"}

    result = convert_to_rub(transaction)
    assert result == 100.0


def test_convert_to_rub_invalid_currency(mock_requests_get):
    # Проверка с невалидной валютой
    with pytest.raises(ValueError, match="Unsupported currency: ABC"):
        transaction = {"amount": 100, "currency": "ABC"}
        convert_to_rub(transaction)
