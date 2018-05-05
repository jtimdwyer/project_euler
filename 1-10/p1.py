#the function below will return the sum of all the integers i in [1,n-1]
#where i is a multiple of 3 or 5
def p1(n):
    s = 0
    for i in range(1,n):
        if (i % 3) == 0 or (i % 5) == 0:
            s += i
    return s

if __name__ == '__main__':
    n = input('Upper bound for terms in sum : ')
    n = int(n)
    print(p1(n))
