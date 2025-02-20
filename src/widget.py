# Основная логика виджета
from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета.
    """
    parts = data.rsplit(" ", 1)  # Разделяем по последнему пробелу (чтобы не потерять 'Visa Platinum')
    if len(parts) != 2:
        raise ValueError("Неверный формат входных данных")

    name, number = parts
    if name.lower().startswith("счет"):
        masked_number = get_mask_account(int(number))  # Присваиваем один раз
    else:
        masked_number = get_mask_card_number(int(number))  # Присваиваем один раз

    return f"{name} {masked_number}"


def get_date(date_str: str) -> str:
    """
    Форматирует дату из '2024-03-11T02:26:18.671407' в '11.03.2024'.
    """
    return datetime.fromisoformat(date_str).strftime("%d.%m.%Y")
