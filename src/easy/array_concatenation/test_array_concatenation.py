# https://leetcode.com/problems/palindrome-number/

from . import array_concatenation


def test_1_array_concatenation():
    numbers: list[int] = [1, 2, 1]
    result: list[int] = array_concatenation(numbers)

    assert result == [1, 2, 1, 1, 2, 1]


def test_2_array_concatenation():
    numbers: list[int] = [1, 3, 2, 1]
    result: list[int] = array_concatenation(numbers)

    assert result == [1, 3, 2, 1, 1, 3, 2, 1]
