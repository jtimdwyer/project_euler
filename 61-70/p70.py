from sympy.ntheory.factor_ import totient
from sympy import sieve
from collections import Counter
import numpy as np


def anagram(p1, p2):
    return Counter(str(p1)) == Counter(str(p2))


def wrapper(lower, upper):
    r = range(lower, upper)
    totient_gen = sieve.totientrange(lower, upper)
    totient_gen = zip(r, totient_gen)
    ratios = [
        (n, phi, n/phi) for n, phi in totient_gen if anagram(n, phi)
    ]
    min_index = np.array([x[2] for x in ratios]).argmin()
    print(ratios[min_index])

if __name__ == "__main__":
    lower = 2
    upper = 10**7
    wrapper(lower, upper)
