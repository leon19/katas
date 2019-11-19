from datetime import datetime

from app.messages import is_stop_message, is_palindrome_message
from app.printer import show_greeting_message, show_farewell_message, show_reversed, show_palindrome_message


class App:
    def __init__(self, name: str, date: datetime) -> None:
        self._name = name
        self._date = date
        self._running = False

    def is_running(self):
        return self._running

    def start(self):
        self._running = True
        show_greeting_message(self._name, self._date)

    def stop(self):
        if not self._running:
            raise RuntimeError('the app is not running')

        self._running = False
        show_farewell_message(self._name)

    def handle_message(self, user_input):
        if is_stop_message(user_input):
            self.stop()
            return

        show_reversed(user_input)

        if is_palindrome_message(user_input):
            show_palindrome_message()
