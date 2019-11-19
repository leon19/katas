from datetime import datetime

from app.messages import get_message_by_time
from app.reverser import reverse

PALINDROME_MESSAGE = '¡Bonita palabra!'


def show_greeting_message(name: str, date: datetime) -> None:
    print(get_message_by_time(date, name))


def show_reversed(text: str) -> None:
    print(reverse(text))


def show_palindrome_message() -> None:
    print(PALINDROME_MESSAGE)


def show_farewell_message(name: str) -> None:
    print(f"¡Adiós {name}!")
