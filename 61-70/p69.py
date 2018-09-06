from sympy import sieve
import numpy as np

if __name__ == "__main__":
    lower = 1
    upper = 1_000_000
    totient_gen = enumerate(sieve.totientrange(lower, upper))
    ratios = [n/phi for n, phi in totient_gen]
    print(np.argmax(ratios) + 1)
