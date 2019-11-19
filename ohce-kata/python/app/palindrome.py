from app.reverser import reverse


def is_palindrome(text: str) -> bool:
    return text == reverse(text)
