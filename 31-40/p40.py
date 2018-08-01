from collections import deque
import time

def find_digits(lst):
    """
    consider the irrational number obtained by putting all
    of the integers together after a decimal points, i.e.
    n = .123456789101112131415...

    if lst is a sequence of non-negatig integers, this returns the digits
    in the fractional part of n with those indexes. For example if lst = [0,1,4]
    then return [1,2,5]
    """
    max_index = max(lst)

    if isinstance(max_index, int):
        max_index = max(max_index, 1)
    else:
        max_index = 1
    out = []
    cur_integer = 0

    while len(''.join(out)) <= max_index:
        cur_integer += 1
        out.append(str(cur_integer))

    out = ''.join(out)
    return [int(out[i]) for i in lst]

if __name__ == "__main__":
    lst = [0, 9, 99, 999, 9999, 99999, 999999]
    lst = find_digits(lst)
    p = 1
    for x in lst:
        p *= x
    print(p)
