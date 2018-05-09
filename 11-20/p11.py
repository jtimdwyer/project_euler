#given a matrix M and an integer k, among all the ways to choose k entries
#in the matrix that are contiguous, be it in the same row, column or diagonal,
# what is the largest product of those terms?

#naively we can do this by iterating over rows, columns and diagonals
#of course this leads to repition, say when we consider all the columns after
#having examind the rows, we're looking at every entry multiple times

#suppose M is a matrix with r row and c columns, represented as a list of
#r rows each of which has length c.
from itertools import product
from collections import defaultdict, deque

def grid_looper(M):
    r,c = len(M), len(M[0])
    for i,j in product(range(r), range(c)):
        yield M[i][j], i, j

#as we loop over the entries in the matrix, we can keep track of windows for
#rows, columns, diagonals, and anti-diagonals and similarly maximum
#window products as we go just keep a deque running for each of these.
#We only need one for the rows since we finish rows as we go, whereas the
#columns and some of the diagonals, don't finish until we enter the final row.

def prod(lst):
    p = 1
    for x in lst:
        p *= x
    return p

#window_helper should adjust the window in question and return a new product
#if the window is long enough. If the window is long enough it returns negative
#infinity.

def window_helper(window, new_value, k):
    window.append(new_value)
    tmp = None
    #this is the first time the window gets to length k
    if len(window) == k:
        tmp = prod(window)
    #this is the loop for each entry that gets added to the window
    #after the first time the window hits length k
    elif len(window) == k + 1:
        old_term = window.popleft()
        tmp = prod(window)

    if tmp:
        return tmp
    else:
        return float('-inf')


def prod_grid(M, k):
    row_window = defaultdict(deque)
    col_window = defaultdict(deque)
    diag_window = defaultdict(deque)
    anti_diag_window = defaultdict(deque)

    grid_max = float('-inf')

    for new_value, r, c in grid_looper(M):
        tmp_r = window_helper(row_window[r], new_value, k)
        tmp_c = window_helper(col_window[c], new_value, k)
        tmp_d = window_helper(diag_window[r-c], new_value, k)
        tmp_ad = window_helper(anti_diag_window[r+c], new_value, k)
        grid_max = max(tmp_r, tmp_c, tmp_d, tmp_ad, grid_max)

    return grid_max

if __name__ == "__main__":
    with open('11.txt') as file:
        M = [[int(entry) for entry in line.split()] for line in file]
    print(prod_grid(M,4))
