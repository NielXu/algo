'''
Problem:
Given an unsorted list s={s1, s2, s3, ..., sn} such that all elements
in the list are in random order. Sort the list in ascending order, which
means if there exists element si and sj, if 1 <= i < j <= n, then si <= sj.

Ideas:
The idea of insertion sort is actually similar with bubble sort. It starts from
the first element and assume it is sorted, then, it takes the next element and
compare it with the first element and perfrom swapping if the first element is
greater than the second. Keep repeating until the list is looped through, and
the element will be sorted.

Time Complexcity:
O(n^2) where n is the length of the given list
'''
def insertion(s):
    for i in range(1, len(s)):
        for j in range(i, 0, -1):
            if s[j] < s[j-1]:
                swap(s, j, j-1)
            else:
                break
    return s

def swap(s, i, j):
    s[i], s[j] = s[j], s[i]

print(insertion([8,9,7,6,0,1]))
print(insertion([9, -13, -12, -12, 33, 0, -13, 97, -100]))
print(insertion([1]))
print(insertion([1,0]))