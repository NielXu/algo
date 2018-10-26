'''
Problem:
Given an unsorted list s={s1, s2, s3, ..., sn} such that all elements
in the list are in random order. Sort the list in ascending order, which
means if there exists element si and sj, if 1 <= i < j <= n, then si <= sj.

Ideas:
Radix sort is a non-comparative integer sorting algorithm that sorts data with
integer keys by grouping keys by the individual digits which share the same
significant position and value. [Wikipedia]

Time Complexity:
O(wn) where n is the length of the given list, and w the word size.

Addition:
This algorithm does not have any optimization.
'''
def _radix_sort_helper(lst, place):
    """ (list of int, int) -> list of int
    Given a list and the place that is going to be sorted,
    return the list that is sorted by bins in ascending order.
    """
    bins = [[], [], [], [], [], [], [], [], [], []]

    # put all elements of cloned list in bins
    for num in lst:

        # find digit and put in bin
        digit = num // (10)**(place - 1) % 10
        bins[digit].append(num)

    # put nums in bin out to sorted list
    sorted_list = (bins[0] + bins[1] + bins[2] + bins[3] +
                   bins[4] + bins[5] + bins[6] + bins[7] +
                   bins[8] + bins[9])

    # return the list
    return sorted_list


def radix_sort(lst):
    """ (list of int) -> list of int
    Return a sorted list in non-decreasing order using the
    radix sort.

    >>> radix_sort([240, 28, 5, 18, 140, 2])
    [2, 5, 18, 28, 140, 240]
    """

    # get max number of list and get the length of it
    longest_int_len = len(str(max(lst)))

    # do steps for longest_int_len amount of times
    for i in range(1, longest_int_len + 1):
        lst = _radix_sort_helper(lst, i)

    # return the list
    return lst
