# https://leetcode.com/problems/plus-one/


def plus_one(digits: list[int]) -> list[int]:
    output = int("".join(str(digit) for digit in digits))
    output += 1

    return [int(entry) for entry in str(output)]
