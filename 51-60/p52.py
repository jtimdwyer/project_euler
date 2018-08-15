def multiple_checker(x, num_of_multiples):
    return len({tuple(sorted(list(str(i*x)))) for i in range(1, num_of_multiples+1)}) == 1



if __name__ == "__main__":
    num_of_multiples = int(input())

    x = 0
    while True:
        x += 1
        if multiple_checker(x, num_of_multiples):
            print(x)
            break