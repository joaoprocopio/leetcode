# https://leetcode.com/problems/shortest-palindrome/


def shortest_palidrome(string: str) -> str:
    reverse: str = string[::-1]

    for index in range(len(reverse)):
        if string.startswith(reverse[index:]):
            return reverse[:index] + string

    return reverse + string
