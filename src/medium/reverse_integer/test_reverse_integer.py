# https://leetcode.com/problems/reverse-integer/

from . import reverse_integer


def test_1_reverse_integer():
    input: int = 123
    output: int = reverse_integer(input)

    assert output == 321


def test_2_reverse_integer():
    input: int = -123
    output: int = reverse_integer(input)

    assert output == -321


def test_3_reverse_integer():
    input: int = 120
    output: int = reverse_integer(input)

    assert output == 21
