"""
Problem:
Interval Scheduling

Given a set of intervals, find a maximum cardinality feasible set,
i.e. no two intervals in the set will overlap each other.
Each interval has a start time s(i) and end time f(i).

Ideas:
Using greedy algorithm. Create an empty set A, sort the intervals by
their finish times. For each interval check if it overlaps with intervals
in A, if not add it to A.

Time Complexity:
O(nlogn) where n is the number of intervals
"""
from math import inf


def interval_scheduling(intervals):
    a = set()
    f = -inf
    sorted_intervals = sorted(intervals, key=lambda x : x[1])
    for i in sorted_intervals:
        if i[0] >= f:
            a.add(i)
            f = i[1]
    return a


intervals = [(2, 5), (3, 7), (4, 6), (2, 3), (5, 9), (10, 99)]
print(interval_scheduling(intervals))

intervals = [(1, 2), (2, 3), (3, 4), (4, 5)]
print(interval_scheduling(intervals))

intervals = [(1, 3), (2, 4), (3, 5), (4, 6)]
print(interval_scheduling(intervals))

intervals = [(1, 5), (2, 6), (3, 7), (4, 8)]
print(interval_scheduling(intervals))
