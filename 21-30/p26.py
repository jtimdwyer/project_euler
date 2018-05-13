#compute decimal period of 1/n

#the idea is this, we should get rid of any 2s or 5s that divide n
#after we've done that, we should find the smallest k such that
#10**k % n == 1, then this k is the decimal period

def decimal_period(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return decimal_period(int(n/2))
    elif n % 5 == 0:
        return decimal_period(int(n/5))
    else:
        counter = 1
        modular_order = 10 % n

        while modular_order != 1:
            modular_order = (10*modular_order)
            modular_order = modular_order % n
            counter += 1
        return counter


if __name__ == '__main__':
    d = int(input('d = '))
    max_period = 0
    num = 0
    for n in range(1,d):
        tmp_period = decimal_period(n)
        if tmp_period > max_period:
            max_period = tmp_period
            num = n
#num is the desired answer
    print(max_period, num)
