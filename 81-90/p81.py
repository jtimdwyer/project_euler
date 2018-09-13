from itertools import product
import csv


def path_sum_two(matrix):
    path_value = {(0, 0): matrix[0][0]}
    r, c = len(matrix), len(matrix[0])

    # fill the values of the first columns
    for i in range(1, r):
        path_value[(i, 0)] = (
            matrix[i][0] + path_value[(i-1, 0)]
        )

    # fill the values of the first row
    for i in range(1, c):
        path_value[(0, i)] = (
            matrix[0][i] + path_value[(0, i-1)]
        )

    # now that the base cases have been filled, we can do the rest.
    for i, j in product(range(1, r), range(1, c)):
        path_value[(i, j)] = (
            matrix[i][j]
            + min(
                path_value[(i-1, j)],
                path_value[(i, j-1)]
            )
        )

    return path_value


def row_fixer(row):
    return [*map(lambda x: int(x.strip()), row)]


with open("./p081_matrix.txt", "r") as f:
    csv_reader = csv.reader(f)
    m = [row_fixer(row) for row in csv_reader]

print(path_sum_two(m)[(len(m)-1,)*2])
