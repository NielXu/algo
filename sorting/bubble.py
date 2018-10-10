'''
Problem:
Given an unsorted list s={s1, s2, s3, ..., sn} such that all elements
in the list are in random order. Sort the list in ascending order, which
means if there exists element si and sj, if 1 <= i < j <= n, then si <= sj.

Ideas:
Bubble sort is the easiest solutoin but meanwhile the slowest solution.
It compares each element with its next element, and perform swapping if
the next element is greater than the current element.

Time Complexcity:
O(n^2) where n is the length of the given list

Addition:
This algorithm does not have any optimization.
'''
def bubble_sort(s):
    for _ in range(0, len(s)-1):
        for j in range(0, len(s)-1):
            if s[j] > s[j+1]:
                swap(s, j, j+1)
    return s

def swap(s, i, j):
    s[i], s[j] = s[j], s[i]

print(bubble_sort([8,9,7,6,0,1]))
print(bubble_sort([9, -13, -12, -12, 33, 0, -13, 97, -100]))
print(bubble_sort([1]))
print(bubble_sort([1,0]))