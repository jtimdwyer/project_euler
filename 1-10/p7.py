#build a prime generator
#as long as n >= 6, the nth prime is < n(ln(n) + ln(ln(n))))
#we'll use the Sieve of Era. on the range of numbers there, and then when
#we're done, return the nth term once we've found it


#the sympy module for this is much faster.

from math import log

def sieve(n):
    if n >= 6:
        upper_bound = n * (log(n) + log(log(n)))
    else:
        d = {
        1:2,
        2:3,
        3:5,
        4:7,
        5:11,
        }
        return d[n]

    ran = {*range(2, int(upper_bound) + 1)}

    which_prime = 0
    while which_prime < n:
        prime = min(ran)
        ran = {x for x in ran if x % prime != 0}
        which_prime += 1

    return prime

if __name__ == "__main__":
    n = input('Which prime do you want? \n')
    n = int(n)
    print(sieve(n))
