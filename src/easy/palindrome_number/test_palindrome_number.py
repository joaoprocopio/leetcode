# https://leetcode.com/problems/palindrome-number/

from . import palindrome_number


def test_1_palindrome_number():
    number: int = 121
    result: bool = palindrome_number(number)

    assert result is True


def test_2_palindrome_number():
    number: int = -121
    result: bool = palindrome_number(number)

    assert result is False


def test_3_palindrome_number():
    number: int = 10
    result: bool = palindrome_number(number)

    assert result is False
