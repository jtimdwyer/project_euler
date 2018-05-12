#generates fibonacci numbers < n
import math

def fib_gen_forever(a=0,b=1):
    yield a
    while True:
        yield b
        a, b = b, a + b

if __name__ == "__main__":
    n = int(input('n = '))
    for ind, fib in enumerate(fib_gen_forever(a=1,b=1),1):
        if len(str(fib)) == n:
            print(ind)
            break
