import json
import logging
import os

from pathlib import Path


# Создаем папку logs, если её нет
os.makedirs("logs", exist_ok=True)

# Настраиваем логер
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

# Хэндлер для записи в файл (перезаписывается при запуске)
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Формат логов
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Добавляем хэндлер к логеру
logger.addHandler(file_handler)


def read_json(file_path: str) -> list:
    """
    Читает JSON-файл и возвращает список транзакций.
    Если файл пустой, отсутствует или содержит некорректные данные, возвращает пустой список.
    """
    path = Path(file_path)
    if not path.exists():
        return []

    try:
        with path.open(encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, FileNotFoundError):
        return []
