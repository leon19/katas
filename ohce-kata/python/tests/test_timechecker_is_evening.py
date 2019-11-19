from app.timechecker import is_evening
from ._helpers import _get_date_at_hour


def test_is_evening_should_return_true_when_the_time_is_between_12_00_and_20_00():
    date = _get_date_at_hour(13)

    assert is_evening(date) is True


def test_is_evening_should_return_true_when_the_time_is_exactly_12_00():
    date = _get_date_at_hour(12)

    assert is_evening(date) is True


def test_is_evening_should_return_false_when_the_time_is_exactly_20_00():
    date = _get_date_at_hour(20)

    assert is_evening(date) is False


def test_is_evening_should_return_false_when_the_time_is_lower_than_12_00():
    date = _get_date_at_hour(11, minute=59)

    assert is_evening(date) is False


def test_is_evening_should_return_false_when_the_time_is_higher_than_20_00():
    date = _get_date_at_hour(21)

    assert is_evening(date) is False

