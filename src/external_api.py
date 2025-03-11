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

    # Убедимся, что возвращаемое значение — это тип float
    return float(data["result"])


def convert_to_rub(transaction: Dict[str, float]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Транзакция с полями "amount" и "currency".
    :return: Сумма транзакции в рублях.
    """
    amount = transaction["amount"]
    currency = transaction["currency"]

    # Убедимся, что валюта - это строка
    if not isinstance(currency, str):
        raise ValueError(f"Currency should be a string, but got {type(currency)}")

    # Если валюта уже в рублях, возвращаем сумму как есть
    if currency == "RUB":
        return float(amount)

    # Конвертируем валюту в рубли
    exchange_rate = get_exchange_rate(currency)

    # Возвращаем сумму в рублях (тип float)
    return float(amount * exchange_rate)
