from unittest.mock import patch

import pytest  # Необходимо для использования pytest
import requests  # Необходимо для работы с requests

from src.external_api import get_exchange_rate  # Убедитесь, что путь правильный


# Тестируем успешный случай получения курса валюты
def test_get_exchange_rate_success() -> None:
    """Тест для успешного получения курса валюты"""
    # Мокаем запрос к API
    with patch("requests.get") as mock_get:
        # Создаем мокаемый ответ
        mock_response = mock_get.return_value
        mock_response.status_code = 200  # Статус успешного ответа
        mock_response.json.return_value = {"result": "75.0"}  # Мокаем результат из API

        # Проверяем, что возвращаемое значение равно ожидаемому
        result = get_exchange_rate("USD")
        assert result == 75.0  # Ожидаем, что курс будет 75.0


# Тестируем случай, когда валюта не поддерживается
def test_get_exchange_rate_invalid_currency() -> None:
    """Тест для случая не поддерживаемой валюты"""
    with pytest.raises(ValueError):
        get_exchange_rate("GBP")  # Проверяем несуществующую валюту


# Тестируем случай, когда API возвращает ошибку
def test_get_exchange_rate_api_error() -> None:
    """Тест для случая ошибки API"""
    with patch("requests.get") as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 400  # Статус ошибки
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Bad Request")

        with pytest.raises(requests.exceptions.HTTPError):
            get_exchange_rate("USD")  # Проверка выброса ошибки
