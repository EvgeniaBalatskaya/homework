import os
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()
API_KEY = os.getenv("EXCHANGE_API_KEY")


def convert_to_rub(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в рубли (RUB).

    :param transaction: Словарь с данными о транзакции (ключи: amount, currency)
    :return: Сумма в рублях (float)
    """
    amount = transaction.get("amount")
    currency = transaction.get("currency")

    # Если уже RUB, просто возвращаем сумму
    if currency == "RUB":
        return float(amount)

    # Проверяем, есть ли ключ API
    if not API_KEY:
        raise ValueError("API-ключ для обменного курса не найден!")

    # Запрос к API курсов валют
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"
    headers = {"apikey": API_KEY}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        rate = data["rates"]["RUB"]
        return float(amount) * rate
    except requests.RequestException as e:
        print(f"Ошибка запроса к API: {e}")
        return 0.0  # В случае ошибки возвращаем 0
