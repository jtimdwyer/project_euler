#returns the set of amicable numbers a, b where a < n

from sympy import divisors

def sum_of_proper_div(n):
    s = -n
    for d in divisors(n):
        s += d
    return s

def find_amicables(n):
    amicables = set()
    for a in range(n):
        b = sum_of_proper_div(a)
        if sum_of_proper_div(b) == a and a != b:
            amicables.update({a,b})
    return amicables

if __name__ == "__main__":
    n = int(input("n = "))
    gen = (x for x in find_amicables(n) if x < n)
    print(sum(gen))
