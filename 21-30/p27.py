from sympy.ntheory.primetest import isprime
from itertools import product

def polynomial_gen(a,b):
    n = 0
    while True:
        yield n**2 + a*n + b
        n += 1

def prime_run(a,b):
    poly_gen = polynomial_gen(a,b)
    count = 0
    while True:
        value = next(poly_gen)
        if isprime(value):
            count += 1
        else:
            break
    return count


if __name__ == "__main__":
    a_bound = int(input('|a| < '))
    b_bound = int(input('|b| <= '))


value = 0
a_out,b_out = 0,0

for a,b in product(range(-a_bound+1,a_bound), range(-b_bound, b_bound+1)):
    tmp = prime_run(a,b)
    if tmp > value:
        value = tmp
        a_out,b_out = a,b
print(a_out*b_out)
