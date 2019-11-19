from datetime import datetime


def is_morning(date: datetime):
    return date.hour >= 6 and date.hour < 12
