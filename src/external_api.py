import os

from typing import Optional

import requests

from dotenv import load_dotenv


# Загружаем переменные окружения из .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://apilayer.com/exchangerates_data-api"


def get_exchange_rate(currency: str) -> Optional[float]:
    """
    Получает текущий курс валюты по отношению к рублю.

    :param currency: Валюта (USD, EUR).
    :return: Курс валюты к рублю или None, если запрос не удался.
    """
    if currency not in {"USD", "EUR"}:
        return None

    params = {"access_key": API_KEY, "symbols": "RUB", "base": currency}

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        rate = data["rates"].get("RUB")
        if isinstance(rate, (int, float)):
            return float(rate)
        return None
    except (requests.RequestException, KeyError, ValueError):
        return None
