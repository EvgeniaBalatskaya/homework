import json
import logging
import os

from pathlib import Path


# Создаем папку logs, если её нет
os.makedirs("../logs", exist_ok=True)

# Настраиваем логер для модуля utils
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

# Хэндлер для записи в файл (перезаписывается при запуске)
file_handler = logging.FileHandler("../logs/utils.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Формат логов
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Добавляем хэндлер к логеру
logger.addHandler(file_handler)

# Логируем старт работы модуля
logger.debug("Инициализация модуля utils")


def read_json(file_path: str) -> list:
    """
    Читает JSON-файл и возвращает список транзакций.
    Если файл пустой, отсутствует или содержит некорректные данные, возвращает пустой список.
    """
    path = Path(file_path)
    logger.info(f"Попытка прочитать файл: {file_path}")

    # Проверяем, существует ли файл
    if not path.exists():
        logger.warning(f"Файл не существует: {file_path}")
        return []

    try:
        with path.open(encoding="utf-8") as file:
            data = json.load(file)
            # Если данные не в формате списка, возвращаем пустой список
            if isinstance(data, list):
                logger.info(f"Успешно прочитан файл: {file_path}, количество транзакций: {len(data)}")
                return data
            else:
                logger.warning(f"Неверный формат данных в файле {file_path}: ожидался список, получен {type(data)}")
                return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка в формате JSON в файле: {file_path}")
        return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except Exception as e:
        logger.error(f"Неизвестная ошибка при чтении файла {file_path}: {e}")
        return []
