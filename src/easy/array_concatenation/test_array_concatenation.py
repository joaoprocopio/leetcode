# https://leetcode.com/problems/concatenation-of-array/

from . import array_concatenation


def test_1_array_concatenation():
    input: list[int] = [1, 2, 1]
    output: list[int] = array_concatenation(input)

    assert output == [1, 2, 1, 1, 2, 1]


def test_2_array_concatenation():
    input: list[int] = [1, 3, 2, 1]
    output: list[int] = array_concatenation(input)

    assert output == [1, 3, 2, 1, 1, 3, 2, 1]
