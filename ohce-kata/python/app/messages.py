from datetime import datetime

from app.timechecker import is_morning, is_evening, is_night


def get_morning_message(name: str) -> str:
    return f"¡Buenos días {name}!"


def get_evening_message(name: str) -> str:
    return f"¡Buenas tardes {name}!"


def get_night_message(name: str) -> str:
    return f"¡Buenas noches {name}!"


def get_message_by_time(date: datetime, name: str) -> str:
    if is_morning(date):
        return get_morning_message(name)

    if is_evening(date):
        return get_evening_message(name)

    if is_night(date):
        return get_night_message(name)
