# https://leetcode.com/problems/largest-rectangle-in-histogram/


def largest_rectangle_in_histogram(heights: list[int]) -> int:
    highest: list[int] = [0, 0]

    for i in range(len(heights) - 1):
        if (heights[i] > highest[0]) and (heights[i + 1] > highest[1]):
            highest[0], highest[1] = heights[i], heights[i + 1]

    return min(highest) * 2
