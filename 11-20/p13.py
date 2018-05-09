if __name__ == "__main__":
    s = 0
    with open('p13.txt') as file:
        for line in file:
            s += int(line)
    print(str(s)[:10])
