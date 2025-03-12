import logging
import os


# Создаем папку logs, если её нет
os.makedirs("logs", exist_ok=True)

# Настраиваем логер для модуля masks
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
    try:
        logger.info(f"Маскируем номер карты: {card_number}")
        card_str = str(card_number)  # Преобразуем в строку
        if len(card_str) != 16:
            logger.error(f"Неверная длина номера карты: {card_number}")
            return "Ошибка: Неверный формат номера карты"
        masked_card = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
        logger.info(f"Маскированный номер карты: {masked_card}")
        return masked_card
    except Exception as e:
        logger.error(f"Ошибка при маскировке номера карты {card_number}: {e}")
        return "Ошибка: Неизвестная ошибка"


def get_mask_account(account_number: int) -> str:
    """Возвращает маску номера счета в формате **XXXX."""
    try:
        logger.info(f"Маскируем номер счета: {account_number}")
        account_str = str(account_number)
        if len(account_str) < 4:
            logger.error(f"Неверная длина номера счета: {account_number}")
            return "Ошибка: Неверный формат номера счета"
        masked_account = f"**{account_str[-4:]}"  # Показываем только последние 4 цифры
        logger.info(f"Маскированный номер счета: {masked_account}")
        return masked_account
    except Exception as e:
        logger.error(f"Ошибка при маскировке номера счета {account_number}: {e}")
        return "Ошибка: Неизвестная ошибка"


# Тесты
print(get_mask_card_number(7000792289606361))  # Должно вывести: 700079** **** 6361
print(get_mask_account(73654108430135874305))  # Должно вывести: **4305
