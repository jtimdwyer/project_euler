if __name__ == "__main__":
    num = int(input())
    print(sum(i**i for i in range(1,num+1)) % 10**10)