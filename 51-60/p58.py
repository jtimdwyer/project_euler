from sympy import sieve

def generate_diagonals(a_max = None):
    # an infinite generator that yields tuples (a,b,c,d)
    # where this tuple are the four diagonal terms on the n by n spiral matrix,
    # n>=3 and n is odd
    # for examply the first response (3,5,7,9)
    # the second is (13, 17, 21, 25)
    
    n = 3
    a,b,c,d = 3,5,7,9
    
    while True:
        yield a,b,c,d
        a += 4 * (n - 1) + 2
        b = a + n + 1
        c = b + n + 13
        d = c + n + 1
        n += 2
        if a_max and a_max < a:
            break
        
        
if __name__ == "__main__":
    prime_proportion_threshold = float(input())
    
    primes_in_diag = set()
    diag_size = 1
    
    for new_diags in generate_diagonals():
        primes_in_diag.update({p for p in new_diags if p in sieve})
        diag_size += 4
        prime_proportion = len(primes_in_diag)/diag_size
        
        if prime_proportion < prime_proportion_threshold:
            break

    print(prime_proportion, (diag_size+1)/2)