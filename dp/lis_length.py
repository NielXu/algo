'''
Problem:
We have a random list S={s1, s2,..., sn}, we want to
find the length of list k where k is the longest sublist of S and
every elements in k are in strictly increasing order, which
means if kj, k(j+1) are two elements in k, then kj < k(j+1).
In other word, we want to find the length of k where k
is the longest increasing subsequence of S.

Ideas:
This problem can be solved by dynamic programming.
We can make a n*n table T, where n is the length of S.
The row of T is S and the column of T is also S.
We place 1 to the diagonal line and then we start iterating,
for each element on the row at index i
we iterate each element on the column at index j:
1. If S[i] <= S[j], we set T[i][j] = 1
2. If S[i] > S[j], we set T[i][j] = max{T[j]}+1
After all iterations, the max number of the table will
be the length of longest increasing subsequence.

Time Complexity:
O(n^2) where n is the length of the given list

Addition:
This algorithm is to find the length of the lis, but not the lis
'''
def lis(s):
    dp = []
    for i in range(len(s)):
        row = []
        for j in range(len(s)):
            row.append(1) if i == j else row.append(0)
        dp.append(row)
    for i in range(len(s)):
        for j in range(i):
            if s[i] <= s[j]:
                dp[i][j] = 1
            else:
                dp[i][j] = max(dp[j]) + 1
    return max(max(x) for x in dp)

print(lis([3,5,7,1,2,8]))
print(lis([1,2,3,4,5,6,7,8]))
print(lis([1]))
print(lis([1,2,1,2,1]))
