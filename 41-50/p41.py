#Find the largest $n$ such that there is an $n$-pandigital prime number.
#For example
from itertools import permutations
from sympy.ntheory import isprime

def pandigital_primes(n):
    """
    returns the largest n-pandigital prime, if it exists

    if there are no n-pandigital primes, returns None

    Example:
    pandigital_primes(2) = None since bth 12 and 21 are composit
    and pandigital_primes(4) = 4231 since this is the largest pandigital prime
    with the numbers 1,2,3,4.
    """
    chars = {f'{i}' for i in range(1,n+1)}
    max_pan_prime = 0
    for x in permutations(chars):
        x = int(''.join(x))
        if isprime(x):
            max_pan_prime = max(x, max_pan_prime)
    if max_pan_prime > 0:
        return max_pan_prime


if __name__ == "__main__":
    for n in range(1,10):
        print(n, pandigital_primes(n))
