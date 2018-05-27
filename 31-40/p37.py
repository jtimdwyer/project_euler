from sympy.ntheory.generate import nextprime
from sympy import isprime

def truncate(p):
    if p in {2,3,5,7}:
        return False

    p_str = str(p)

    for ind in range(1,len(p_str)):
        trunc_l = int(p_str[ind:])
        trunc_r = int(p_str[:ind])
        both_prime = isprime(trunc_l) and isprime(trunc_r)
        if not both_prime:
            return False
    return True

if __name__ == "__main__":
    count = 0
    p = 11
    trunc_primes = set()
    while len(trunc_primes) < 11:
        if truncate(p):
            trunc_primes.add(p)
        p = nextprime(p)
    print(sum(trunc_primes))
