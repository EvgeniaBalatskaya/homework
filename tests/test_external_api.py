from unittest.mock import mock_open, patch

from src.external_api import read_json


def test_read_json_valid():
    # Мокаем содержимое файла
    mock_data = '[{"amount": 100, "currency": "RUB"}]'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_json("data/operations.json")
        assert result == [{"amount": 100, "currency": "RUB"}]  # Ожидаем правильный список


def test_read_json_empty():
    # Мокаем пустой файл
    mock_data = ""
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_json("data/operations.json")
        assert result == []  # Ожидаем пустой список


def test_read_json_invalid():
    # Мокаем некорректный JSON
    mock_data = "not a json"
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_json("data/operations.json")
        assert result == []  # Ожидаем пустой список


def test_read_json_not_a_list():
    # Мокаем данные, которые не являются списком
    mock_data = '{"amount": 100, "currency": "RUB"}'  # Это объект, а не список
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_json("data/operations.json")
        assert result == []  # Ожидаем пустой список, так как данные не список
