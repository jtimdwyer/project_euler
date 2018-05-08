#we'll return the sum of the primes <= n
#again I'm sure the sympy generator for primes is faster.

def sieve(n):
    ran = [*range(2, n)]
    while ran:
        prime = ran[0]
        ran = [x for x in ran if x % prime != 0]
        yield prime

if __name__ == '__main__':
    n =int(input('n = '))
    print(sum(sieve(n)))
