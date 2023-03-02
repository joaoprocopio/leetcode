# https://leetcode.com/problems/palindrome-number/

from . import palindrome_number


def test_1_palindrome_number():
    input: int = 121
    output: bool = palindrome_number(input)

    assert output is True


def test_2_palindrome_number():
    input: int = -121
    output: bool = palindrome_number(input)

    assert output is False


def test_3_palindrome_number():
    input: int = 10
    output: bool = palindrome_number(input)

    assert output is False
