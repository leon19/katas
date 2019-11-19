from datetime import datetime

from app.timechecker import is_morning


def test_is_morning_should_return_true_when_the_time_is_between_06_00_and_12_00():
    date = _get_date_at_hour(7)

    assert is_morning(date) is True


def _get_date_at_hour(hour: int) -> datetime:
    return datetime(year=2019, month=1, day=1, hour=hour)
