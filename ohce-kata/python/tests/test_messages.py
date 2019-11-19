from app.messages import get_morning_message, get_night_message, get_evening_message


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
