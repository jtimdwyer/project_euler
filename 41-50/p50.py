from sympy import sieve
import numpy as np

def primes_consecutive_sums(sieve, upper_bound):
    sieve.extend(upper_bound)    
    primes_list = list(sieve.primerange(1,upper_bound))
    primes_set = set(primes_list)

    
    primes_cum_sum = np.cumsum(primes_list)
    primes_cum_sum = np.append([0], primes_cum_sum)

    
    
    
    #let's look at the possible lengths of sums
    #start with the biggest, we're doing a lot of dumb work!
    #we don't need to check what we get from the sum of like 4 primes :(
    

    for d in range(len(primes_list), 1, -1):
        consec_sums_tmp = set(primes_cum_sum[d:] - primes_cum_sum[:-d])
        consec_sums_tmp.intersection_update(primes_set)
        if consec_sums_tmp:
            return consec_sums_tmp
        

        
if __name__ == "__main__":
    upper_bound = int(input())
    print(primes_consecutive_sums(sieve, upper_bound))
    