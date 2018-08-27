from fractions import Fraction

def e_cont_frac():
    """
    Yields the encoded continued fraction
    of e
    """
    c, even = 0, 2
    yield 2
    yield 1
    while True:
        if c % 3 == 0:
            yield even
            even += 2
        else:
            yield 1
        c += 1



def numerator_denom(cont_gen, num_terms):
    """
    Returns the list of the first num_terms
    convergents corresponding to the encoded
    continued fraction cont_gen
    """
    a = [next(cont_gen), next(cont_gen)]

    h, k = [a[0], a[1]*a[0]+1], [1, a[1]]

    for _ in range(2, num_terms):
        a.append(next(cont_gen))
        h.append(a[-1]*h[-1] + h[-2])
        k.append(a[-1]*k[-1] + k[-2])

    return [Fraction(x,y) for x,y in zip(h,k)]


if __name__ == "__main__":
    x = numerator_denom(e_cont_frac(), 100)[-1].numerator
    print(sum(map(int, list(str(x)))))