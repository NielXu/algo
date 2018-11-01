'''
Problem:
We have some $1 $3 and $5, how many coins do we need at least
to make $11.

Extension:
This problem can be extended to: given a list of coins with
values {c1, c2, c3, ..., ck}, how many coins do we need at least
to make n

Ideas:
Suppose C(a) = n, where a is the sum we need and n
is the least coins require to get the sum a.
C(0) = 0, we need no coins to make $0
C(1) = C(1-1)+1 = C(0)+1 = 1, we need one $1 to make $1
C(2) = C(2-1)+1 = C(1)+1 = 2, we need two $1 to make $2
C(3) = min{C(3-1)+1 = C(2)+1 = 3, C(3-3)+1 = C(0) + 1 = 1} = 1, we need one $3 to make $3
C(4) = min{C(4-1)+1 = C(3)+1 = 2} = 2,we need one $1 and one $3 to make $4
...
We can observe that, the state-transition-equation can
be defined as: C(i) = min{C(i-j)+1}, where i-j >= 0 and i represents
the least coins require to get the sum i, and j represents the value
of the jth coin.

Time Complexity:
O(n*m) where n is the sum and m is the number of coins
'''
def dp_coin(coins, coin_sum):
    table = [0]
    for i in range(1, coin_sum+1):
        table.append(i)
    for i in range(1, coin_sum+1):
        for j in range(len(coins)):
            if i >= coins[j] and table[i-coins[j]]+1 < table[i]:
                table[i] = table[i - coins[j]] + 1
    return table[coin_sum]

print(dp_coin([1,3,5], 11))
print(dp_coin([1,2,3], 11))
print(dp_coin([1,2,3,4], 121))