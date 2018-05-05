#find the largest palindrome that is the product of two n-digit numbers.

from itertools import product

def palindrome_finder(n):
    max_pal = 0
    for x,y in product(range( 10**(n-1), 10**n ),repeat=2):
        num = x*y
        s = str(num)
        if s == s[::-1] and num > max_pal:
            max_pal = num
    return max_pal

if __name__ == "__main__":
    n = input('How many digits would you like to use? ')
    n = int(n)
    print(palindrome_finder(n))
