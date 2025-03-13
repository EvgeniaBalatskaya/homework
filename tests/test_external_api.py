from typing import Dict


def convert_to_rub(rates: Dict[str, float]) -> float:
    rub_rate = rates.get("RUB", 1.0)
    return rub_rate
