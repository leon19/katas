from datetime import datetime

from app.messages import get_message_by_time
from app.palindrome import is_palindrome
from app.reverser import reverse

PALINDROME_MESSAGE = '¡Bonita palabra!'
STOP_MESSAGE = 'Stop!'


class App:
    def __init__(self, name: str, date: datetime) -> None:
        self._name = name
        self._date = date

    def show_greeting_message(self) -> None:
        print(get_message_by_time(self._date, self._name))

    def ask_for_input(self) -> str:
        return input('> ')

    def print_reversed(self, user_input: str) -> None:
        print(reverse(user_input))

    def show_palindrome_message_if_needed(self, user_input: str) -> None:
        if not is_palindrome(user_input):
            return

        print(PALINDROME_MESSAGE)

    def is_stop_message(self, user_input: str) -> bool:
        return user_input == STOP_MESSAGE

    def show_farewell_message(self):
        print(f"¡Adiós {self._name}!")
