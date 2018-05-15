from itertools import product

def distinct_powers(a_upper, b_upper):
    pows = set()
    for a,b in product(range(2,a_upper + 1), range(2,b_upper + 1)):
        pows.add(a**b)
    return pows

if __name__ == "__main__":
    a_upper = int(input('a <= '))
    b_upper = int(input('b <= '))
    out = len(distinct_powers(a_upper, b_upper))
    print(out)
