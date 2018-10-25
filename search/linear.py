'''
Problem:
We have a list s={s1, s2, s3, ..., sn}, we want to
find the index of an element si(1 <= i <= n). If si
appears multiple times, just return the first index
it appears. If there is no such element, return -1.

Ideas:
Simple linear search, from index 0 to index n. Compare
each element with the target using ==, if they are equal,
return the index and end the method. Otherwise, return -1
at the end of the method.

Time Complexity:
O(n), where n is the len of the given list
'''
def linear(s, target):
    for i in range(0, len(s)):
        if s[i] == target:
            return i
    return -1

print(linear([0,1,2,3], 1))
print(linear([112.6, 144.01, -15.75, 11.48, -98.5], 100))
print(linear([], 99))
