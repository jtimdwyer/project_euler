#This question can be interpteed as asking for pairs (n,d) with 1 <= n < d <= 1,000,000
#and gcd(n,d) = 1. This is just the sum of the totient numbers between 2 and 1,000,001

from sympy import sieve

upper = 1_000_000 + 1
print(sum(sieve.totientrange(2, upper)))