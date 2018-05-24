def double_pal_check(n):
    n_str = str(n)
    n_bin = bin(n)[2:]
    dec_pal = (n_str == n_str[::-1])
    bin_pal = (n_bin == n_bin[::-1])
    return dec_pal and bin_pal

if __name__ == "__main__":
    k = int(input('n = '))
    print(sum(n for n in range(1,k) if double_pal_check(n)))
