# https://leetcode.com/problems/largest-rectangle-in-histogram/

from . import largest_rectangle_in_histogram


def test_1_largest_rectangle_in_histogram():
    input: list[int] = [2, 1, 5, 6, 2, 3]
    output: int = largest_rectangle_in_histogram(input)

    assert output == 10


def test_2_largest_rectangle_in_histogram():
    input: list[int] = [2, 4]
    output: int = largest_rectangle_in_histogram(input)

    assert output == 4
