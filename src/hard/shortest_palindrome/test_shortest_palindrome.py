# https://leetcode.com/problems/shortest-palindrome/


from . import shortest_palidrome


def test_1_shortest_palidrome():
    input: str = "aacecaaa"
    output: str = shortest_palidrome(input)

    assert output == "aaacecaaa"


def test_2_shortest_palidrome():
    input: str = "abcd"
    output: str = shortest_palidrome(input)

    assert output == "dcbabcd"
