'''
Problem:
We have a list s={s1, s2, s3, ..., sn} that is SORTED,
we want to find the index of an element si(1 <= i <= n).
If si appears multiple times, the returned index will base
on the length of the list, and it WILL NOT ALWAYS return the first
index. If there is no such element, return -1.

Restriction:
The given list MUST BE SORTED

Ideas:
Using binary search we can reduce time from O(n) to O(log(n)).
However, this algorithm can only be applied on sorted list.
The idea is, assume the list is S and the target we are looking for
is t, we start from the mid index, which is len(S)//2 = k. If S[k] == t,
the method will stop and return k. Otherwise, if t > S[k], search the
list from k to len(S), if t < S[k] search the list from 0 to k. Keep doing this
process recursively until we find the index of the target.

Time Complexcity:
O(log(n))
'''
def bin_search(s, target):
    return perform(s, target, 0, len(s))

def perform(s, target, low, high):
    mid = low + (high - low) // 2
    if mid == -1 or mid == len(s):
        return -1
    if s[mid] == target:
        return mid
    elif target > s[mid]:
        return perform(s, target, mid+1, high)
    else:
        return perform(s, target, low, mid-1)

print(bin_search([0,1,2,3,4], 3))
print(bin_search([10,17,22,34,39,40], 1))
print(bin_search([1], 1))
print(bin_search([10,15,17], 20))
print(bin_search([10,15,17,18,29,33], 33))
print(bin_search([0.8,7.1,8.2,9.909], 0.8))
print(bin_search([10], 0))
print(bin_search([0, 12, 30, 34, 55, 66, 66, 66], 66))