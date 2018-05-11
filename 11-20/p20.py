def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

if __name__ == "__main__":
    n = int(input("n = "))
    out = str(factorial(n))
    out =[ int(x) for x in list(out)]
    print(sum(out))
