from datetime import datetime
from unittest.mock import patch, MagicMock

from app.messages import get_morning_message, get_night_message, get_evening_message, get_message_by_time, \
    is_stop_message, STOP_MESSAGE, is_palindrome_message


def test_get_morning_message_should_correctly_format_the_message():
    name = 'Lorens'
    message = get_morning_message(name)

    assert message == "¡Buenos días Lorens!"


def test_get_evening_message_should_correctly_format_the_message():
    name = 'Lorens'
    message = get_evening_message(name)

    assert message == "¡Buenas tardes Lorens!"


def test_get_night_message_should_correctly_format_the_message():
    name = 'Lorens'
    message = get_night_message(name)

    assert message == "¡Buenas noches Lorens!"


@patch('app.messages.get_morning_message', spec=True)
@patch('app.messages.is_night', spec=True, return_value=False)
@patch('app.messages.is_evening', spec=True, return_value=False)
@patch('app.messages.is_morning', spec=True, return_value=True)
def test_get_message_by_time_should_return_the_morning_message(mocked_is_morning: MagicMock,
                                                               mocked_is_evening: MagicMock,
                                                               mocked_is_night: MagicMock,
                                                               mocked_get_morning_message: MagicMock):
    date = datetime.now()
    name = 'Lorens'

    expected_message = ''
    mocked_get_morning_message.return_value = expected_message

    message = get_message_by_time(date, name)

    assert message == expected_message

    mocked_is_morning.assert_called_with(date)
    mocked_get_morning_message.assert_called_with(name)


@patch('app.messages.get_evening_message', spec=True)
@patch('app.messages.is_night', spec=True, return_value=False)
@patch('app.messages.is_evening', spec=True, return_value=True)
@patch('app.messages.is_morning', spec=True, return_value=False)
def test_get_message_by_time_should_return_the_evening_message(mocked_is_morning: MagicMock,
                                                               mocked_is_evening: MagicMock,
                                                               mocked_is_night: MagicMock,
                                                               mocked_get_evening_message: MagicMock):
    date = datetime.now()
    name = 'Lorens'

    expected_message = ''
    mocked_get_evening_message.return_value = expected_message

    message = get_message_by_time(date, name)

    assert message == expected_message

    mocked_is_evening.assert_called_with(date)
    mocked_get_evening_message.assert_called_with(name)


@patch('app.messages.get_night_message', spec=True)
@patch('app.messages.is_night', spec=True, return_value=True)
@patch('app.messages.is_evening', spec=True, return_value=False)
@patch('app.messages.is_morning', spec=True, return_value=False)
def test_get_message_by_time_should_return_the_night_message(mocked_is_morning: MagicMock,
                                                             mocked_is_evening: MagicMock,
                                                             mocked_is_night: MagicMock,
                                                             mocked_get_night_message: MagicMock):
    date = datetime.now()
    name = 'Lorens'

    expected_message = ''
    mocked_get_night_message.return_value = expected_message

    message = get_message_by_time(date, name)

    assert message == expected_message

    mocked_is_night.assert_called_with(date)
    mocked_get_night_message.assert_called_with(name)


def test_is_stop_message_should_return_true_when_the_message_is_the_correct_stop_message():
    assert is_stop_message(STOP_MESSAGE) is True


def test_is_stop_message_should_return_false_when_the_message_is_not_the_correct_stop_message():
    assert is_stop_message('some random message') is False


def test_is_palindrome_should_return_true_when_the_input_is_a_palindrome():
    assert is_palindrome_message('somos') is True
    assert is_palindrome_message('recocer') is True
    assert is_palindrome_message('erre') is True
    assert is_palindrome_message('ojo') is True


def test_is_palindrome_should_return_false_when_the_input_is_not_a_palindrome():
    assert is_palindrome_message('echo') is False
    assert is_palindrome_message('adios') is False
    assert is_palindrome_message('aqui') is False
    assert is_palindrome_message('hola') is False
