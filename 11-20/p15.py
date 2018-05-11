def two_n_choose_n(n):
    if n == 1:
        return 2
    else:
        return int((2*n)*(2*n-1)*two_n_choose_n(n-1)/(n**2))

if __name__ == "__main__":
    n = int(input('n = '))
    print(two_n_choose_n(n))
