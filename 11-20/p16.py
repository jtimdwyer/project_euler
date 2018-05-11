def sum_of_dig(n):
    num = (int(char) for char in iter(str(2**n)))
    return sum(num)

if __name__ == "__main__":
    n = int(input("what power of 2 "))
    print(sum_of_dig(n))
