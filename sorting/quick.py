'''
Problem:
Given an unsorted list s={s1, s2, s3, ..., sn} such that all elements
in the list are in random order. Sort the list in ascending order, which
means if there exists element si and sj, if 1 <= i < j <= n, then si <= sj.

Ideas:
There are three steps of quicksort:
Suppose the list is S
1. Select a pivot in the list, say it is p
2. For all elements in the list, if S[i] < p, place S[i]
to the left side of p, if S[i] > p, place S[i] to the
right side of p. And after this process, we let elements
that are on the left side of p be a partition k, elements
that are on the right side of p be a partition j
3. Repeat step 1 and 2 for both k and j, until the lengths
of k and j are one.

Time Complexity:
O(nlogn) where n is the length of the given list

Addition:
Quicksort is not stable, since it exchanges nonadjacent elements.
'''
def quick(s):
    return perform(s, 0, len(s)-1)

def perform(s, left, right):
    if left < right:
        pivot = partition(s, left, right)
        perform(s, left, pivot-1)
        perform(s, pivot+1, right)
    return s

def partition(s, left, right):
    pivot = s[right]
    i = left-1
    for j in range(left, right):
        if s[j] <= pivot:
            i += 1
            swap(s, i, j)
    swap(s, i+1, right)
    return i+1

def swap(s, i, j):
    s[i], s[j] = s[j], s[i]

print(quick([8,9,7,6,0,1]))
print(quick([9, -13, -12, -12, 33, 0, -13, 97, -100]))
print(quick([1]))
print(quick([1,0]))
