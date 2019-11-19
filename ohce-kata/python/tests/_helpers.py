from datetime import datetime


def _get_date_at_hour(hour: int, minute: int = 0) -> datetime:
    return datetime(year=2019, month=1, day=1, hour=hour, minute=minute)
