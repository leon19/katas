from unittest.mock import patch

from app.palindrome import is_palindrome


def test_is_palindrome_should_return_true_when_the_input_is_a_palindrome():
    assert is_palindrome('somos') is True
    assert is_palindrome('recocer') is True
    assert is_palindrome('erre') is True
    assert is_palindrome('ojo') is True


def test_is_palindrome_should_return_false_when_the_input_is_not_a_palindrome():
    assert is_palindrome('echo') is False
    assert is_palindrome('adios') is False
    assert is_palindrome('aqui') is False
    assert is_palindrome('hola') is False
