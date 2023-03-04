# https://leetcode.com/problems/reverse-integer/


def reverse_integer(x: int) -> int:
    if x > 0:
        return int(str(x)[::-1])
    if x < 0:
        return -int(str(x).replace("-", "")[::-1])

    return x
