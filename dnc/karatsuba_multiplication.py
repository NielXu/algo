"""
Problem:
Multiplication in a more efficient way

Given two number x and y, calculate their product x*y in less than
O(n^2) running time.

Ideas:
Using Karatsuba Multiplication algorithm. Convert x and y into
binary and divide them into two parts. x = x1 * 2^(n/2) + x0,
y = y1 * 2^(n/2) + y0.
   x*y = x1*y1*(2^n) + (x1*y0 + x0*y1)^(2^(n/2)) + x0*y0
=> x*y = x1*y1*(2^n) + ((x1+x0) * (y1+y0) - (x1*y1) - (x0*y0))*(2^(n/2)) + x0*y0
In this way only three multiplications are needed:
P1 = x1*y1
P2 = x0*y0
P3 = (x1+x0)*(y1+y0).
According to the Master Theorem (https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)),
the running time can be reduced to O(n^(log2(3))) < O(n^2).

Time Complexity:
O(n^(log2(3))) where n is the bit length
"""
import math


def karatsuba_multiplication(x, y):
   return mul(format(x, 'b'), format(y, 'b'))


def bits_add(x, y):
   return format(int(x, 2) + int(y, 2), 'b')


def mul(x, y):
   n = max(len(x), len(y))
   n_floor = math.floor(n/2)
   n_ceil = math.ceil(n/2)
   if n == 1:
      return int(x) * int(y)
   x = x.zfill(n)
   y = y.zfill(n)
   xL = x[:n_ceil]
   xR = x[n_ceil:]
   yL = y[:n_ceil]
   yR = y[n_ceil:]
   p1 = mul(xL, yL)
   p2 = mul(xR, yR)
   p3 = mul(bits_add(xL, xR), bits_add(yL, yR))
   return p1 * (2 ** (2 * n_floor)) + (p3 - p2 - p1) * (2 ** n_floor) + p2


print(karatsuba_multiplication(38, 25))

print(karatsuba_multiplication(3999, 1))

print(karatsuba_multiplication(55, 125))

print(karatsuba_multiplication(490, 2680))

print(karatsuba_multiplication(38123476, 2512845))
