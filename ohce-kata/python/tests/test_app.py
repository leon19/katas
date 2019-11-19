from datetime import datetime
from unittest.mock import patch, MagicMock

from app.app import App


@patch('builtins.print')
@patch('app.app.get_message_by_time')
def test_app_show_greeting_message(mocked_get_message_by_time: MagicMock, mocked_print: MagicMock):
    name = 'Lorens'
    date = datetime.now()

    expected_message = ''
    mocked_get_message_by_time.return_value = expected_message

    app = App(name, date)
    app.show_greeting_message()

    mocked_get_message_by_time.assert_called_with(date, name)
    mocked_print.assert_called_with(expected_message)


@patch('builtins.input')
def test_app_ask_for_input(mocked_input):
    name = 'Lorens'
    date = datetime.now()

    expected_input = ''
    mocked_input.return_value = expected_input

    app = App(name, date)
    user_input = app.ask_for_input()

    mocked_input.assert_called_with('> ')
    assert user_input == expected_input


@patch('builtins.print')
@patch('app.app.reverse')
def test_print_reversed(mocked_reverse: MagicMock, mocked_print: MagicMock):
    text = 'echo'
    reversed_text = 'ohce'
    name = 'Lorens'
    date = datetime.now()

    mocked_reverse.return_value = reversed_text
    app = App(name, date)

    app.print_reversed(text)

    mocked_reverse.assert_called_with(text)
    mocked_print.assert_called_with(reversed_text)
