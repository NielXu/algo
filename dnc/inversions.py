"""
Counting inversions of an array with a divide and conquer algorithm.

We define an inversion as follows: a[i] < a[j] for j < i, where a is an array.
"""
from typing import List


def _inversions_between(a: List[int], b: List[int]) -> int:
    """
    Count the inversions between `a` and `b` using the mergesort.

    If b has a smaller element than a, then there exists an inversion between it and all the elements
    in the sorted list.
    """
    # sort the two lists in O(nlogn) time.
    sa = sorted(a)
    sb = sorted(b)

    # keep track of index
    i, j, inversions = 0, 0, 0
    while i < len(sa) and j < len(sb):
        if sa[i] <= sb[j]:
            i += 1
        else:
            j += 1
            inversions += len(sa) - i
    return inversions


def num_inversions(lst: List[int]) -> int:
    """
    Return the number of inversions of `lst`.

    Idea
    ====
    the number of inversions of 2 sublist + the number of inversions betweeen sublist.

    The Running time: O(nlogn)

    >>> num_inversions([1, 2, 3])
    0
    >>> num_inversions([1, 3, 2])
    1
    >>> num_inversions([1, 3, 5, 2, 4, 6])
    3
    """
    # base case when there is one element
    if len(lst) == 1:
        return 0
    # base case when there are two elements
    elif len(lst) == 2:
        return int(lst[0] > lst[1])
    # recursive step
    else:
        # split into left and right
        left = lst[:len(lst) // 2]
        right = lst[len(lst) // 2:]

        # count the inversions on left and right
        left_inversions = num_inversions(left)
        right_inversions = num_inversions(right)

        # add the inversions between them
        return left_inversions + right_inversions + _inversions_between(left, right)
