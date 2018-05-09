from math import sqrt

def divisor_count(n):
    number_of_div = 0
    sqr_root = int(sqrt(n))
    #count the divisors that are not sqrt(n)
    for div in range(1,sqr_root):
        if n % div == 0:
                number_of_div += 2
    #check if sqrt(n) is a divisor
    if n == sqr_root**2:
        number_of_div += 1

    return number_of_div

if __name__ == "__main__":
    k = input('find the first triangular number more than k divisors\n k =  ')
    k = int(k)
    tri_num,n = 1,1

    while True:
        if divisor_count(tri_num) > k:
            break
        else:
            n += 1
            tri_num += n

    print(tri_num)
