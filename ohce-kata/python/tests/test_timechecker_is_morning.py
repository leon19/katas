from datetime import datetime


def test_is_morning_should_return_true_when_the_time_is_between_06_00_and_12_00():
    date = datetime(year=2019, month=1, day=1, hour=21)

    assert is_morning(date) is True
