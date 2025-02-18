def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета в переданной строке.

    :param data: строка с типом и номером карты/счета
    :return: строка с замаскированным номером
    """
    match = re.search(r'(.+?)\s(\d+)', data)
    if not match:
        raise ValueError("Некорректный формат данных")

    card_type, number = match.groups()
    if "Счет" in card_type:
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{card_type} {masked_number}"


def get_date(timestamp: str) -> str:
    """
    Преобразует строку с датой в формат ДД.ММ.ГГГГ.

    :param timestamp: строка с датой в формате "2024-03-11T02:26:18.671407"
    :return: строка в формате "11.03.2024"
    """
    try:
        date_obj = datetime.fromisoformat(timestamp[:10])
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Некорректный формат даты")
