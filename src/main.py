from datetime import datetime
from typing import Dict, List

from src.file_processing.reader import read_csv_transactions, read_excel_transactions
from src.file_processing.utils import read_json
from src.transactions import filter_transactions_by_description


def format_transaction(transaction: Dict[str, str]) -> str:
    """
    Форматирует транзакцию для вывода.
    """
    date = datetime.strptime(transaction["date"], "%Y-%m-%dT%H:%M:%S").strftime("%d.%m.%Y")
    description = transaction["description"]
    amount = f'{transaction["amount"]} {transaction["currency"]}'

    sender = transaction.get("from", "Неизвестный источник")
    receiver = transaction.get("to", "Неизвестный получатель")

    return f"{date} {description}\n{sender} -> {receiver}\nСумма: {amount}"


def main(test_mode: bool = False, test_inputs: list[str] = None) -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    input_index = 0  # Указатель для тестовых вводов
    def get_input(prompt: str) -> str:
        nonlocal input_index
        if test_mode and test_inputs:
            response = test_inputs[input_index]
            input_index += 1
            print(f"input() вызван с prompt: {prompt} - response: {response}")  # Логируем вызов input
            return response
        return input(prompt)

    while True:
        print("\nВыберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        print("4. Выйти")

        choice = get_input("Ваш выбор: ")

        if choice == "4":
            print("Выход из программы.")
            break

        if choice == "1":
            file_path = get_input("Введите путь к JSON-файлу: ")
            transactions = read_json(file_path)
        elif choice == "2":
            file_path = get_input("Введите путь к CSV-файлу: ")
            transactions = read_csv_transactions(file_path)
        elif choice == "3":
            file_path = get_input("Введите путь к XLSX-файлу: ")
            transactions = read_excel_transactions(file_path)
        else:
            print("Неверный выбор. Попробуйте снова.")
            continue

        if not transactions:
            print("Ошибка: не удалось загрузить транзакции. Проверьте файл и повторите попытку.")
            continue

        valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
        while True:
            print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
            print(f"Доступные для фильтрации статусы: {', '.join(valid_statuses)}")
            status = get_input("Ваш статус: ").upper()

            if status in valid_statuses:
                break
            print(f'Статус операции "{status}" недоступен.')

        filtered_transactions = [t for t in transactions if t.get("status", "").upper() == status]
        print(f'\nОперации отфильтрованы по статусу "{status}"')

        if get_input("\nОтсортировать операции по дате? Да/Нет ").strip().lower() == "да":
            order = get_input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
            reverse = order == "по убыванию"
            try:
                filtered_transactions.sort(
                    key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S"), reverse=reverse
                )
                print("Операции отсортированы.")
            except ValueError:
                print("Ошибка сортировки: неверный формат даты.")

        if get_input("\nВыводить только рублевые транзакции? Да/Нет ").strip().lower() == "да":
            filtered_transactions = [t for t in filtered_transactions if t.get("currency", "").upper() == "RUB"]

        if get_input("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет ").strip().lower() == "да":
            search_word = get_input("Введите слово для поиска в описании: ")
            filtered_transactions = filter_transactions_by_description(filtered_transactions, search_word)

        print("\nРаспечатываю итоговый список транзакций...")
        if filtered_transactions:
            print(f"\nВсего банковских операций в выборке: {len(filtered_transactions)}\n")
            for transaction in filtered_transactions:
                print(format_transaction(transaction))
                print("-" * 40)
        else:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
