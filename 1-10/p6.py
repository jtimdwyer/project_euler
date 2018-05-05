#trying to return (1+2+...+n)^2 - (1^2 + 2^2 + ... + n^2)
#but of course 1 + 2 + ... + n = n(n+1)/2
#and 1^2 + 2^2 + ... + n^2 = n(n+1)(2n+1)/6

def sum_of_square(n):
    return int(n*(n+1)*(2*n+1)/6)

def square_of_sum(n):
    return int(n*(n+1)/2)**2

if __name__ == "__main__":
    n = input("""
    difference between sum of squares and square of sum  of [1,n]\n
    n = """)
    n = int(n)
    print(square_of_sum(n) - sum_of_square(n))
