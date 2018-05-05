#generates the fibonacci numbers <= n, beginning with 0 and 1
def fibonacci_gen(n):
    a,b = 0,1
    yield a
    yield b
    if n >= 2:
        c = b + a
        while c <= n:
            yield c
            a = b
            b = c
            c = a + b

#this will return the sum of the even fib numbers which are <= n
def sum_even_fibs(n):
    s = 0
    for fib in fibonacci_gen(n):
        if fib % 2 == 0:
            s += fib
    return s

if __name__ == '__main__':
    n = input('What is the upper bound on Fibonacci numbers you would like?\n')
    print(sum_even_fibs(int(n)))
