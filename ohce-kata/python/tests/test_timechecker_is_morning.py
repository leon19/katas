from datetime import datetime

from app.timechecker import is_morning


def test_is_morning_should_return_true_when_the_time_is_between_06_00_and_12_00():
    date = _get_date_at_hour(7)

    assert is_morning(date) is True


def test_is_morning_should_return_true_when_the_time_is_exactly_06_00():
    date = _get_date_at_hour(6)

    assert is_morning(date) is True


def test_is_morning_should_return_false_when_the_time_is_exactly_12_00():
    date = _get_date_at_hour(12)

    assert is_morning(date) is False


def test_is_morning_should_return_false_when_the_time_is_lower_than_06_00():
    date = _get_date_at_hour(5, minute=59)

    assert is_morning(date) is False


def test_is_morning_should_return_false_when_the_time_is_higher_than_12_00():
    date = _get_date_at_hour(13)

    assert is_morning(date) is False


def _get_date_at_hour(hour: int, minute: int = 0) -> datetime:
    return datetime(year=2019, month=1, day=1, hour=hour, minute=minute)
