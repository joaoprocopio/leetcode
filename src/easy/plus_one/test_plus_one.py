# https://leetcode.com/problems/plus-one/

from . import plus_one


def test_1_plus_one():
    input: list[int] = [1, 2, 3]
    output: list[int] = plus_one(input)

    assert output == [1, 2, 4]


def test_2_plus_one():
    input: list[int] = [4, 3, 2, 1]
    output: list[int] = plus_one(input)

    assert output == [4, 3, 2, 2]


def test_3_plus_one():
    input: list[int] = [9]
    output: list[int] = plus_one(input)

    assert output == [1, 0]


# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]


# Input: digits = [9]
# Output: [1,0]
