from collections import Counter
def pan_digital_check(s):
    """
    for s > 0, determine if there is a pan digital
    number which can be formed as the concatednated
    product of s with some (1,2,...,n) where n > 1

    If this product exists, return it, else returns None
    """
    def is_pandigital(num):
        """
        checks if a number is pan-digital
        """
        nums = Counter({'1', '2', '3', '4', '5', '6', '7', '8', '9'})
        return Counter(str(num)) == nums

    concat_list = []
    for i in range(10**9):
        concat_list.append(str(s*i))
        tmp = int(''.join(concat_list))
        if is_pandigital(tmp):
            return tmp
        elif tmp > 987654321:
            return


if __name__ == "__main__":
    max_pan = 0
    for s in range(1, 10**4):
        new_pan = pan_digital_check(s)
        if new_pan:
            max_pan = max(max_pan, new_pan)
    print(max_pan)
