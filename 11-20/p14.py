def collatz(n):
    while n > 1:
        yield n
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = 3 * n + 1
    yield n

if __name__ == "__main__":
    k = input("upper bound for starting points in the collatz sequence ")
    k = int(k)
    len_max = 0
    start_max = 0
    for start in range(k):
        tmp = 0
        for _ in collatz(start):
            tmp += 1
        if tmp > len_max:
            start_max = start
            len_max = tmp
    print(start_max)
