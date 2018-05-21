# If n is a number that can be writter n = a * b where the digits 1 through 9
# all appear precisely onces in n, a and b then the product n is said to be
# a pan digital product.
#
# Find the sum of all the products that are pan digital. It is possible that
# n = a * b and n = c * d are truly different products but this product should
# only be counted once.
#
#
#If a product n = a * b where a < b, then it must be the case that a is a two
#digit number, b is a three digit number and n is a four digit number. This
#narrows our search greatly. We can just geneerate all permutation of 1..9
#declare that a is the first two digits, b is the next 3 and n is the remaining
#four. Then we see if n = a * b, and if it is we add it to a set keeping track
#of everything.

from itertools import permutations, product, combinations


#this will generate all triples of integers a,b,n which have every
#integer 1,2,...9 collectively. For example at some point the generator
#will yield the truple (12,37,8956)

def pan_digital_gen():
    perm_gen = permutations(range(1,10))
    comps = combinations(range(1,9),2)

    for pi, comp in product(perm_gen, comps):
        a = pi[:comp[0]]
        b = pi[comp[0]:comp[1]]
        n = pi[comp[1]:]

        a, b, n = (str(d) for d in a), (str(d) for d in b), (str(d) for d in n)
        a, b, n = ''.join(a), ''.join(b), ''.join(n)
        a, b, n = int(a), int(b), int(n)
        yield a, b, n

def pan_check():
    pan_prods = set()
    gen = pan_digital_gen()

    for a, b, n in gen:
        if n == a * b:
            pan_prods.add(n)

    return pan_prods

if __name__ == "__main__":
    pan_prods = pan_check()
    print(sum(pan_prods))
