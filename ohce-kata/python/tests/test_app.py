from datetime import datetime
from unittest.mock import patch, MagicMock

from pytest import raises

from app.app import App
from app.messages import STOP_MESSAGE


@patch('app.app.show_greeting_message')
def test_app_start_should_run_and_show_the_greeting_message(mocked_show_greeting_message: MagicMock):
    name = 'Lorens'
    date = datetime.now()

    app = App(name, date)
    app.start()

    mocked_show_greeting_message.assert_called_with(name, date)
    assert app.is_running() is True


@patch('app.app.show_greeting_message')
@patch('app.app.show_farewell_message')
def test_app_stop_should_stop_and_show_the_farewell_message(
    mocked_show_farewell_message: MagicMock,
    mocked_show_greeting_message: MagicMock
):
    name = 'Lorens'
    date = datetime.now()

    app = App(name, date)
    app.start()
    app.stop()

    mocked_show_greeting_message.assert_called_with(name, date)
    mocked_show_farewell_message.assert_called()
    assert app.is_running() is False


def test_app_stop_should_raise_a_runtime_error_when_the_app_is_not_started():
    name = 'Lorens'
    date = datetime.now()

    app = App(name, date)

    with raises(RuntimeError):
        app.stop()


@patch('app.app.show_farewell_message')
@patch('app.app.show_palindrome_message')
@patch('app.app.is_palindrome_message')
@patch('app.app.show_reversed')
@patch('app.app.is_stop_message', return_value=True)
def test_app_handle_input_when_a_stop_message_is_given_the_app_should_stop(
    mocked_is_stop_message: MagicMock,
    mocked_show_reversed: MagicMock,
    mocked_is_palindrome_message: MagicMock,
    mocked_show_palindrome_message: MagicMock,
    mocked_show_farewell_message: MagicMock
):
    name = 'Lorens'
    date = datetime.now()

    app = App(name, date)
    app.start()

    message = STOP_MESSAGE
    app.handle_message(message)

    assert app.is_running() is False
    mocked_is_stop_message.assert_called_with(message)
    mocked_show_farewell_message.assert_called_with(name)

    mocked_show_reversed.assert_not_called()
    mocked_is_palindrome_message.assert_not_called()
    mocked_show_palindrome_message.assert_not_called()


@patch('app.app.show_farewell_message')
@patch('app.app.show_palindrome_message')
@patch('app.app.is_palindrome_message', return_value=False)
@patch('app.app.show_reversed')
@patch('app.app.is_stop_message', return_value=False)
def test_app_handle_input_when_a_message_is_given_the_app_print_the_reversed_message(
    mocked_is_stop_message: MagicMock,
    mocked_show_reversed: MagicMock,
    mocked_is_palindrome_message: MagicMock,
    mocked_show_palindrome_message: MagicMock,
    mocked_show_farewell_message: MagicMock
):
    name = 'Lorens'
    date = datetime.now()

    app = App(name, date)
    app.start()

    message = 'random message'
    app.handle_message(message)

    assert app.is_running() is True
    mocked_show_reversed.assert_called_with(message)


@patch('app.app.show_farewell_message')
@patch('app.app.show_palindrome_message')
@patch('app.app.is_palindrome_message', return_value=True)
@patch('app.app.show_reversed')
@patch('app.app.is_stop_message', return_value=False)
def test_app_handle_input_when_a_palindrome_message_is_given_the_app_print_the_palindrome_message(
    mocked_is_stop_message: MagicMock,
    mocked_show_reversed: MagicMock,
    mocked_is_palindrome_message: MagicMock,
    mocked_show_palindrome_message: MagicMock,
    mocked_show_farewell_message: MagicMock
):
    name = 'Lorens'
    date = datetime.now()

    app = App(name, date)
    app.start()

    message = 'somos'
    app.handle_message(message)

    assert app.is_running() is True
    mocked_is_palindrome_message.assert_called_with(message)
    mocked_show_palindrome_message.asser_called()
