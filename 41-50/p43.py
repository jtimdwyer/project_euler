from itertools import permutations

def div_prop_check(pan_dig):
    """
    For a 0 to 9 pandigital number, pan_dig,
    returns True if the sub-string divisibility property
    defined in problem 43 holds.

    Else return False
    """

    primes = [2,3,5,7,11,13,17]
    pan_dig = str(pan_dig)
    sub_strs = [
        int(pan_dig[start_index+1:start_index+4])
        for start_index in range(len(primes))
    ]

    sub_strs = [sub_str % p == 0 for sub_str, p in zip(sub_strs, primes)]
    return all(sub_strs)

if __name__ == "__main__":
    chars = [str(i) for i in range(0,10)]
    pan_digitals = [int(''.join(p)) for p in permutations(chars) if p[0] != '0']
    pan_digitals = [p for p in pan_digitals if div_prop_check(p)]
    print(sum(pan_digitals))
