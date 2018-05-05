#We'll pritn the largest prime factor of the input n >= 2
from math import sqrt

def largest_prime_fac(n):
    if n == 2:
        return 2
        
    p = 0
    for div in range(2, int(sqrt(n)) + 1):
        while n % div == 0:
            p = div
            n = int(n / div)
#at this point, if current n is 1, then maxprime is the largest prime
#otherwise n is >= 2, and is itself the largest prime factor of the input n
    if n > 2:
        p = n
    return p


if __name__ == '__main__':
    n = input("Find the larges factor of what number? ")
    n = int(n)
    print(largest_prime_fac(n))
