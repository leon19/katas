from datetime import datetime
from unittest.mock import patch, MagicMock

from app.app import App, STOP_MESSAGE, PALINDROME_MESSAGE


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


@patch('builtins.print')
@patch('app.app.is_palindrome', return_value=True)
def test_app_show_palindrome_message_is_needed_should_show_message_when_the_input_is_palindrome(
    mocked_is_palindrome: MagicMock,
    mocked_print: MagicMock):
    user_input = ''
    name = 'Lorens'
    date = datetime.now()

    app = App(name, date)
    app.show_palindrome_message_if_needed(user_input)

    mocked_is_palindrome.assert_called_with(user_input)
    mocked_print.assert_called_with(PALINDROME_MESSAGE)


@patch('builtins.print')
@patch('app.app.is_palindrome', return_value=False)
def test_app_show_palindrome_message_is_needed_should_not_show_any_message_when_the_input_is_not_a_palindrome(
    mocked_is_palindrome: MagicMock,
    mocked_print: MagicMock):
    user_input = ''
    name = 'Lorens'
    date = datetime.now()

    app = App(name, date)
    app.show_palindrome_message_if_needed(user_input)

    mocked_is_palindrome.assert_called_with(user_input)
    assert mocked_print.call_count == 0


def test_app_is_stop_message_should_return_true_when_the_message_is_the_correct_stop_message():
    name = 'Lorens'
    date = datetime.now()

    app = App(name, date)

    assert app.is_stop_message(STOP_MESSAGE) is True


def test_app_is_stop_message_should_return_false_when_the_message_is_not_the_correct_stop_message():
    name = 'Lorens'
    date = datetime.now()

    app = App(name, date)

    assert app.is_stop_message('some random message') is False


@patch('builtins.print')
def test_app_show_farewell_message(mocked_print):
    name = 'Lorens'
    date = datetime.now()

    app = App(name, date)
    app.show_farewell_message()

    mocked_print.assert_called_with(f"¡Adiós {name}!")
