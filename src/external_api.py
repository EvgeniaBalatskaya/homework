import os

from typing import Dict

import requests

from dotenv import load_dotenv


# Загружаем переменные окружения
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"


def get_exchange_rate(currency: str) -> float:
    """
    Получает текущий курс валюты по отношению к рублю.

    :param currency: Валюта (USD или EUR).
    :return: Курс валюты к рублю.
    :raises ValueError: Если валюта не поддерживается.
    """
    if currency not in {"USD", "EUR"}:
        raise ValueError(f"Unsupported currency: {currency}")

    params: Dict[str, str] = {"from": currency, "to": "RUB", "amount": "1"}
    headers = {"apikey": API_KEY}

    response = requests.get(BASE_URL, params=params, headers=headers)
    response.raise_for_status()
    data = response.json()

    # Преобразуем результат в float, если это строка
    result = data.get("result", "0")

    try:
        return float(result)  # Преобразуем строку в float
    except ValueError:
        raise ValueError(f"Unable to convert result to float: {result}")


def convert_to_rub(transaction: Dict[str, float]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Транзакция с полями "amount" и "currency".
    :return: Сумма транзакции в рублях.
    """
    amount = transaction["amount"]
    currency = transaction["currency"]

    if currency == "RUB":
        return amount

    # Убедитесь, что currency передается как строка
    exchange_rate = get_exchange_rate(str(currency))  # Преобразуем в строку, если нужно
    return amount * exchange_rate
