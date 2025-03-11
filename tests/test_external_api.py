import pytest
from unittest.mock import patch
from src.external_api import convert_to_rub

@patch("src.external_api.requests.get")
def test_convert_to_rub_usd(mock_get):
    mock_get.return_value.json.return_value = {"rates": {"RUB": 75.0}}
    mock_get.return_value.status_code = 200

    transaction = {"amount": 10, "currency": "USD"}
    assert convert_to_rub(transaction) == 750.0  # 10 USD * 75 RUB

def test_convert_to_rub_rub():
    transaction = {"amount": 5000, "currency": "RUB"}
    assert convert_to_rub(transaction) == 5000.0
