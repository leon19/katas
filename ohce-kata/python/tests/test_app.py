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
