from typing import Any
from unittest.mock import patch

import pytest

from src.external_api import convert_to_rub, get_exchange_rate


@patch("src.external_api.requests.get")
def test_get_exchange_rate(mock_get) -> None:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"rates": {"RUB": 75.0}}

    assert get_exchange_rate("USD") == 75.0


@pytest.mark.parametrize(
    "transaction, expected",
    [
        ({"amount": 100, "currency": "RUB"}, 100.0),
        ({"amount": 10, "currency": "USD"}, 750.0),  # Если курс 75
        ({"amount": 20, "currency": "EUR"}, 1700.0),  # Если курс 85
    ],
)
@patch("src.external_api.get_exchange_rate", side_effect=lambda x: 75 if x == "USD" else 85)
def test_convert_to_rub(mock_exchange_rate, transaction: dict[str, Any], expected: float) -> None:
    assert convert_to_rub(transaction) == expected


def test_convert_to_rub_invalid_currency() -> None:
    with pytest.raises(ValueError):
        convert_to_rub({"amount": 100, "currency": "GBP"})
