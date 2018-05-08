#find a < b < c with a^2 + b^2 = c^2
#and a + b + c = 1000. return a*b*c

#a^2 + b^2 = (1000 - a - b)^2
#sympy has a nice solver for Diophantine equations, so let's use that!

from sympy import Symbol
from sympy.solvers.diophantine import diophantine

def search_euclid(k):
    triples = set()
    a = Symbol('a')
    b = Symbol('b')
    solns = diophantine(a**2 + b**2 - (k - a - b)**2)

    for a,b in solns:
        if 0 < a < b < k - a:
            pythag_trip = (a, b, k-a-b)
            triples.add(pythag_trip)
    return triples

if __name__ == '__main__':
    k = input('Search for pythagorean triples that sum to k = ')
    k = int(k)
    print(search_euclid(k))
