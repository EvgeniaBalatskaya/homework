from unittest.mock import mock_open, patch

from src.external_api import convert_to_rub, get_exchange_rate
from src.utils import read_json


# Тестирование get_exchange_rate
@patch("src.external_api.requests.get")
def test_get_exchange_rate(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 75.0}

    assert get_exchange_rate("USD") == 75.0


# Тестирование convert_to_rub
@patch("src.external_api.get_exchange_rate", return_value=75.0)
def test_convert_to_rub(mock_get_exchange_rate):
    transaction = {"amount": 10, "currency": "USD"}
    assert convert_to_rub(transaction) == 750.0

    transaction = {"amount": 100, "currency": "RUB"}
    assert convert_to_rub(transaction) == 100.0


# Тестирование чтения JSON-файла
@patch("builtins.open", mock_open(read_data='[{"amount": 100, "currency": "RUB"}]'))
def test_read_json_valid():
    result = read_json("data/operations.json")
    assert result == [{"amount": 100, "currency": "RUB"}]


@patch("builtins.open", mock_open(read_data=""))
def test_read_json_empty():
    result = read_json("data/operations.json")
    assert result == []


@patch("builtins.open", mock_open(read_data="not a json"))
def test_read_json_invalid():
    result = read_json("data/operations.json")
    assert result == []
