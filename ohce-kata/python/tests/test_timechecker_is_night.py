from app.timechecker import is_night
from ._helpers import _get_date_at_hour


def test_is_night_should_return_true_when_the_time_is_between_20_00_and_06_00():
    date = _get_date_at_hour(21)

    assert is_night(date) is True


def test_is_night_should_return_true_when_the_time_is_exactly_20_00():
    date = _get_date_at_hour(20)

    assert is_night(date) is True


def test_is_night_should_return_false_when_the_time_is_exactly_06_00():
    date = _get_date_at_hour(6)

    assert is_night(date) is False


def test_is_night_should_return_false_when_the_time_is_lower_than_20_00():
    date = _get_date_at_hour(19, minute=59)

    assert is_night(date) is False


def test_is_night_should_return_false_when_the_time_is_higher_than_06_00():
    date = _get_date_at_hour(7)

    assert is_night(date) is False
