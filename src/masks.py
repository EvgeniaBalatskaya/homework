import logging
import os


# Создаем папку logs, если её нет
os.makedirs("logs", exist_ok=True)

# Настраиваем логер
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

# Хэндлер для записи в файл (перезаписывается при запуске)
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Формат логов
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Добавляем хэндлер к логеру
logger.addHandler(file_handler)


# Функции для маскировки номеров карт и счетов
def get_mask_card_number(card_number: int) -> str:
    """Возвращает маску номера карты в формате XXXX XX** **** XXXX."""
    card_str = str(card_number)  # Преобразуем в строку
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Возвращает маску номера счета в формате **XXXX."""
    account_str = str(account_number)
    return f"**{account_str[-4:]}"  # Показываем только последние 4 цифры


# Тесты
print(get_mask_card_number(7000792289606361))  # Должно вывести: 700079** **** 6361
print(get_mask_account(73654108430135874305))  # Должно вывести: **4305
