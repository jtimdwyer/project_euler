#5*9^5 = 295245 so if a number

if __name__ == "__main__":
    nums = set()
    for n in range(2,295246):
        if n == sum(int(char)**5 for char in str(n)):
            nums.add(n)
    print(sum(nums))
