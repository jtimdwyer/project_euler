from itertools import product

def digit_sum(n):
    return sum([int(x) for x in str(n)])


if __name__ == "__main__":
    upper_bound = int(input())
    digit_sums = [digit_sum(a**b) for a, b in product(range(upper_bound), repeat=2)]
    print(max(digit_sums))