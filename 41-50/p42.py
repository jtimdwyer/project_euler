def is_triangle_number(T):
    """
    returns True if T is a triangle number,
    otherwise returns False
    """
    disc = (1+8*T)**.5
    n_plus = (-1+disc)/2
    n_plus_int_test = (n_plus == int(n_plus))
    
    return n_plus_int_test

def word_value(word):
    """
    for the string word, returns the sum of the positions of the letters,
    in the sense that A is the first letter in the alphabet, , B is the second,
    so for example word_value('ABDC') = 1+2+4+3 = 10

    Needs to be capitalized
    """
    ord_base = ord('A') - 1
    return sum(ord(char) - ord_base for char in word)


if __name__ == "__main__":
    import csv
    with open('./p042_words.txt', 'r') as csv_file:
        lst = []
        for row in csv.reader(csv_file):
            lst.extend(row)

    lst = [word for word in lst if is_triangle_number(word_value(word))]
    print(len(lst))
