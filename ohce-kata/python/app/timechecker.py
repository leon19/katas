from datetime import datetime

SIX_AM = 6
TWELVE_PM = 12


def is_morning(date: datetime) -> bool:
    return SIX_AM <= date.hour < TWELVE_PM
