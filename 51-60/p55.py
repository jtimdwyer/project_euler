def is_palindrome(n):
    n = str(n)
    return n == n[::-1]

def add_reverse(n):
    return n + int(str(n)[::-1])

def is_not_lychrel(n):
    n = add_reverse(n)
    for _ in range(100):
        if is_palindrome(n):
            return n
        else:
            n = add_reverse(n)

if __name__ == "__main__":
    upper_bound = int(input())
    num_lychrel = len([n for n in range(1, upper_bound+1) if not is_not_lychrel(n)])
    print(num_lychrel)