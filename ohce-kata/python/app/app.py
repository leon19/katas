from datetime import datetime

from app.messages import get_message_by_time


class App:
    def __init__(self, name: str, date: datetime) -> None:
        self._name = name
        self._date = date

    def show_greeting_message(self) -> None:
        print(get_message_by_time(self._date, self._name))
