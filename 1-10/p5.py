#return the smallest number divisible by all the numbers in 1,2,3...,n
#this is also called the least common multiple of these numbers

from math import gcd

#returns the lcm of a pair of numbers
def lcm_pair(a,b):
    return int(a*b/gcd(a,b))

#returns the lcm of a list of numbers
def lcm_list(lst):
    length = len(lst)
    if length >= 1:
        running_lcm = lst[0]
        for c in lst[1:]:
            running_lcm = lcm_pair(running_lcm,c)
    else:
        running_lcm = 0
    return running_lcm


if __name__ == "__main__":
    n = input("Find the lcm of the number 1,2,...,n. n = ? \n")
    n = int(n)
    lst = list(range(1,n+1))
    print(int(lcm_list(lst)))
