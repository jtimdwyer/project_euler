#generates the permutations of n in lexicographic order
#of the digits 0,1,..., n-1

from collections import deque

def perm_gen(n):
    if n == 0:
        yield deque([0])
    else:
        for first_term in range(n+1):
            for r_perm in perm_gen(n-1):
                tmp_perm = deque()
                for entry in r_perm:
                    if entry >= first_term:
                        tmp_perm.append(entry+1)
                    else:
                        tmp_perm.append(entry)
                tmp_perm.appendleft(first_term)
                yield tmp_perm


if __name__ == "__main__":
    n = int(input("n = "))
    k = int(input("k = "))
    for i, perm in enumerate(perm_gen(n)):
        if i == k:
            print(perm)
            break
