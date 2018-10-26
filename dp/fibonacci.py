'''
Problem:
The fibonacci sequence is defined in this way:
Si = {
    0               if i=0
    1               if i=1
    S(i-1) + S(i-2) if i>1
}
which means, the first term of the fibonacci sequence
is 0 and the second term is 1 and start from the third term,
the number will be the sum of the previous two terms.
Given an integr j (j>=0), compute the fibonacci
sequence at index j, which is Sj.

Ideas:
The fibonacci sequence can be computed using recursion very
easily, however, it causes lots of unnecessary calculations
if using recursion. Intead, using dynamic programming, we
can compute the number in a very short time compare with
recursion. We can store the calculated terms in a list so
that next time when we need the numbers, we can get them
directly from the list instead of calculating them again.

Time Complexity:
O(n) where n is the fibonacci number we are looking for

Extra Space:
O(n) where n is the fibonacci number we are looking for
'''
def fib(n):
    s=[0,1]
    for i in range(2, n+1):
        s.append(s[i-1]+s[i-2])
    return s[n]

print(fib(9))
print(fib(0))
print(fib(1))
print(fib(55))
