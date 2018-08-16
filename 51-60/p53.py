from sympy import binomial
from itertools import product

if __name__ == "__main__":
    n_upper = int(input())
    binomial_lower = int(input())
    
    counter = len({
        (n,r) for n,r in product(range(n_upper + 1), repeat=2) 
        if binomial(n,r) > binomial_lower 
    })
    
    print(counter)