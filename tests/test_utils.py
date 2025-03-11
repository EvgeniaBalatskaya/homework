from unittest.mock import mock_open, patch

import pytest

from src.utils import read_json


@pytest.mark.parametrize(
    "file_data, expected",
    [
        ('[{"amount": 100, "currency": "RUB"}]', [{"amount": 100, "currency": "RUB"}]),
        ("{}", []),  # JSON-объект вместо списка
        ("", []),  # Пустой файл
    ],
)
def test_read_json(file_data: str, expected: list[dict]) -> None:
    with patch("builtins.open", mock_open(read_data=file_data)):
        with patch("pathlib.Path.exists", return_value=True):
            with patch("pathlib.Path.is_file", return_value=True):
                assert read_json("data/operations.json") == expected


def test_read_json_file_not_found() -> None:
    with patch("pathlib.Path.exists", return_value=False):
        assert read_json("data/operations.json") == []
