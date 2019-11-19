from datetime import datetime
from unittest.mock import MagicMock, patch

from app.printer import show_greeting_message, show_reversed, show_palindrome_message, PALINDROME_MESSAGE, \
    show_farewell_message


@patch('app.printer.get_message_by_time')
@patch('builtins.print')
def test_printer_show_greeting_message(mocked_print: MagicMock, mocked_get_message_by_time: MagicMock):
    name = ''
    date = datetime.now()

    greeting_message = ''
    mocked_get_message_by_time.return_value = greeting_message

    show_greeting_message(name, date)

    mocked_get_message_by_time.assert_called_with(date, name)
    mocked_print.assert_called_with(greeting_message)


@patch('app.printer.reverse')
@patch('builtins.print')
def test_printer_show_reversed(mocked_print: MagicMock, mocked_reverse: MagicMock):
    text = ''
    reversed_text = 'reversed text'
    mocked_reverse.return_value = reversed_text

    show_reversed(text)

    mocked_reverse.assert_called_with(text)
    mocked_print.assert_called_with(reversed_text)


@patch('builtins.print')
def test_printer_show_palindrome_message(mocked_print: MagicMock):
    show_palindrome_message()

    mocked_print.assert_called_with(PALINDROME_MESSAGE)


@patch('builtins.print')
def test_printer_show_farewell_message(mocked_print: MagicMock):
    name = 'Lorens'
    show_farewell_message(name)

    mocked_print.assert_called_with(f"¡Adiós {name}!")
