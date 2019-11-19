from datetime import datetime

SIX_AM = 6
TWELVE_PM = 12
EIGHT_PM = 20


def is_morning(date: datetime) -> bool:
    return SIX_AM <= date.hour < TWELVE_PM


def is_evening(date: datetime) -> bool:
    return TWELVE_PM <= date.hour < EIGHT_PM
