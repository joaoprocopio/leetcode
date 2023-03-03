# https://leetcode.com/problems/single-number/

from . import single_number


def test_1_single_number():
    input: list[int] = [2, 2, 1]
    output: int = single_number(input)
    assert output == 1


def test_2_single_number():
    input: list[int] = [4, 1, 2, 1, 2]
    output: int = single_number(input)
    assert output == 4


def test_3_single_number():
    input: list[int] = [1]
    output: int = single_number(input)
    assert output == 1
