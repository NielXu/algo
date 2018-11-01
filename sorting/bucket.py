'''
Problem:
Given an unsorted list s={s1, s2, s3, ..., sn} such that all elements
in the list are in random order. Sort the list in ascending order, which
means if there exists element si and sj, if 1 <= i < j <= n, then si <= sj.

Restriction:
Elements in the given list MUST GREATER THAN OR EQUAL TO 0
There is another way to handle the negative case,
but it will not be presented here.

Ideas:
Bucket sort is useful when the given list is
uniformly distributed across a range. The steps are:
Assume given list is S,
1. Create n empty lists where n=len(S)
2. For each element in S -> S[i]
    - insert S[i] into bucket[n*S[i]]
3. Sort each bucket
4. Concatenate all non-empty sorted buckets

Time Complexcity:
O(n+k) where n is the length of the given list,
and k is the range of the number

Extra Space:
O(n) where n is the length of the given list

Addition:
The performance of this algorithm highly depends on
the distribution of the given list, the worst case
can be O(n^2) with O(n) extra space, which is worse
than bubble sort.
'''
def bucket(s):
    # Step is the variable that can be modified based
    # on the given list, we use 10 here as example.
    step = 10
    mi, ma = min(s), max(s)
    n = int(ma/step - mi/step + 1)
    b = [[] for _ in range(n)]
    result = []
    for i in s:
        b[key(i, mi, step)].append(i)
    for i in b:
        if len(i) > 0:
            result.extend(sorted(i))
    return result

def key(i, m, step):
    return int((i-m)/step)

print(bucket([8,9,7,6,0.5,1]))
print(bucket([1.5, 2]))
print(bucket([1]))
print(bucket([1.2, 99, 2001, 14, 3, 0.1922]))
print(bucket([13, 22, 0, 34, 91, 112, 80, 75, 63, 59, 40]))