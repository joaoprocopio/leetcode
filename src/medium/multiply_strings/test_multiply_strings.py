# https://leetcode.com/problems/multiply-strings/

from . import multiply_strings


def test_1_multiply_strings():
    input1: str = "2"
    input2: str = "3"
    output: str = multiply_strings(input1, input2)

    assert output == "6"


def test_2_multiply_strings():
    input1: str = "123"
    input2: str = "456"
    output: str = multiply_strings(input1, input2)

    assert output == "56088"
