from typing import Dict
from unittest.mock import mock_open, patch

import pytest

from src.external_api import convert_to_rub, read_json


def test_read_json_valid() -> None:
    mock_data = '[{"amount": 100.0, "currency": "RUB"}]'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_json("data/operations.json")
        assert result == [{"amount": 100.0, "currency": "RUB"}]  # Ожидаем число, а не строку


def test_read_json_empty() -> None:
    with patch("builtins.open", mock_open(read_data="")):
        result = read_json("data/operations.json")
        assert result == []


def test_read_json_invalid() -> None:
    with patch("builtins.open", mock_open(read_data="not a json")):
        result = read_json("data/operations.json")
        assert result == []


def test_read_json_not_a_list() -> None:
    mock_data = '{"amount": 100.0, "currency": "RUB"}'  # Убедитесь, что это словарь с числами
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_json("data/operations.json")
        assert result == []


def test_convert_to_rub_valid() -> None:
    transaction: Dict[str, float] = {"amount": 100.0, "currency": "USD"}

    with patch("src.external_api.get_exchange_rate", return_value=75.0):
        result = convert_to_rub(transaction)
        assert result == 7500.0


def test_convert_to_rub_already_rub() -> None:
    transaction: Dict[str, float] = {"amount": 100.0, "currency": "RUB"}
    result = convert_to_rub(transaction)
    assert result == 100.0


def test_convert_to_rub_invalid_currency() -> None:
    transaction: Dict[str, float] = {"amount": 100.0, "currency": "GBP"}
    with pytest.raises(ValueError):
        convert_to_rub(transaction)
