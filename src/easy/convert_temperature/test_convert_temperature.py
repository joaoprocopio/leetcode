# https://leetcode.com/problems/convert-the-temperature/

from . import convert_temperature


def test_1_convert_temperature():
    input: float = 36.50
    output: list[float] = convert_temperature(input)

    assert output == [309.65000, 97.70000]


def test_2_convert_temperature():
    input: float = 122.11
    output: list[float] = convert_temperature(input)

    assert output == [395.26000, 251.79800]
