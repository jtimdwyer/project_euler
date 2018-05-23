from sympy import sieve


#for a prime p in primes, tests if all the cyclic rotations are also in primes
def prime_cycle_test(p,primes):
    p_st = str(p)
    cycles = set()
    evens = {'0', '2', '4', '6', '8'}

    #2 is circular
    if p == 2:
        return True

    #to avoid building a bunch of strings we can rule out any prime
    #with an even digit
    for char in evens:
        if char in p_st:
            return False

    for i, _ in enumerate(p_st):
        cycled_p = int(p_st[i:] + p_st[:i])
        if cycled_p not in primes:
            return False

    return True



if __name__ == "__main__":
    a = int(input('a = '))
    b = int(input('b = '))
    primes = set(sieve.primerange(a,b))
    cyc_primes = set()
    for p in primes:
        if prime_cycle_test(p,primes):
            cyc_primes.add(p)
    print(len(cyc_primes))
