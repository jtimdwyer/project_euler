from sympy import divisors
from itertools import product

#returns the set of abundant numbers < n
def find_abundant(n):
    abund = set()
    for num in range(n):
        if sum(divisors(num)) > 2*num:
            abund.add(num)
    return abund

#return a set containgn all the possible sums of two abundant numbers x, y
#where x + y < n
def sum_of_abund(n):
    abund = find_abundant(n)
    out = set()
    for x,y in product(abund, repeat=2):
        if x + y < n:
            out.add(x+y)
    return out

if __name__ == "__main__":
    n = int(input("n = "))
    print(sum([i for i in range(n)]) - sum(sum_of_abund(n)))
