#return the largest product of k adjacent terms in a list

from collections import deque

def prod(lst):
    p = 1
    for x in lst:
        p *= x
    return p

def largest_product_window(lst,k):
    d = deque(lst[:k])
    window = prod(d)
    max_window_prod = window
    for new_term in lst[k:]:
        old_term = d.popleft()
        d.append(new_term)

        if old_term != 0:
            window = int(window*new_term/old_term)
        else:
            window = prod(d)

        if window > max_window_prod:
            max_window_prod = window
    return max_window_prod



if __name__ == "__main__":
    n = input('product of digits of integer : ')
    n = list(n)
    n = [int(digit) for digit in n]

    k = input('how many digits : ')
    k = int(k)

    print(largest_product_window(n,k))
