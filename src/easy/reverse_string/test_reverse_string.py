# https://leetcode.com/problems/reverse-string/

from . import reverse_string


def test_1_reverse_string():
    input: list[str] = ["h", "e", "l", "l", "o"]
    output: list[str] = reverse_string(input)

    assert output == ["o", "l", "l", "e", "h"]


def test_2_reverse_string():
    input: list[str] = ["H", "a", "n", "n", "a", "h"]
    output: list[str] = reverse_string(input)

    assert output == ["h", "a", "n", "n", "a", "H"]
