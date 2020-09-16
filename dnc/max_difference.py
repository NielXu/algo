"""
CSC C73 Midterm, Fall 2017, Question 3.
"""
from typing import List


def max_difference(a: List[int]) -> (int, int):
    """
    We are given an array A[1..n] of integers, n >= 1. We want to find a pair of indices (i, j) such that
    1 <= i <= j <= n and A[j] - A[i] is as large as possible.

    Running Time with Master's Theorem:
    ===================================
    a = 2 (2 subproblems)
    b = 2 (each of half size)
    d = 1 (linear time to calc result)

    a = b^d = 2
    Running time: O(nlogn)

    >>> max_difference([5, 11, 2, 1, 7, 9, 0, 7])
    (1, 9)
    """
    # base case
    if len(a) == 1:
        return a[0], a[0]
    else:
        # split A into half.
        first = a[:len(a)//2]
        second = a[len(a)//2:]

        # 2 sub problems, 1/2 of original size.
        small1, big1 = max_difference(first)
        small2, big2 = max_difference(second)

        # get min of first and max of second
        # linear time
        min_first = min(first)
        max_second = max(second)

        # 3 cases, either (small1, big1), (min_first, max_second), (small2, big2)
        # constant comparisons
        if big2 - small2 > max_second - min_first and big2 - small2 > big1 - small1:
            return small2, big2
        elif big1 - small1 > max_second - min_first:
            return small1, big1
        else:
            return min_first, max_second
