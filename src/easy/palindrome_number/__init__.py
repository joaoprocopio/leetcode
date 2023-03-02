# https://leetcode.com/problems/palindrome-number/


def palindrome_number(number: int) -> bool:
    return str(number) == str(number)[::-1]
