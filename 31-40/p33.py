from itertools import product
from fractions import Fraction

def check_reduce(numer, denom):
    """
    numer and denom should be integers,
    denom != 0, and this checks if there
    is a misleading cancellation, i.e. 
    a digit in both numer and denom which
    when deleted from both, is the same fraction
    """

    numer_str, denom_str = str(numer), str(denom)
    numer_enumerate = enumerate(numer_str)
    denom_enumerate = enumerate(denom_str)
    char_iterator = product(numer_enumerate, denom_enumerate)
    
    def int_try(number_string):
        try:
            return int(number_string)
        except:
            return 0
    for (n_index, n_char), (d_index, d_char) in char_iterator:
        if n_char == d_char and n_char != '0':
            tmp_numer = numer_str[:n_index] + numer_str[n_index+1:]
            tmp_denom = denom_str[:d_index] + denom_str[d_index+1:]
            if int_try(tmp_numer)*denom == numer*int_try(tmp_denom):
                return True
    return False            


if __name__ == "__main__":
    product_fraction = Fraction(1,1)
    for n,d in product(range(10,100), repeat=2):
        if n != d and n/d < 1:
            if check_reduce(n,d):
                product_fraction *= Fraction(n,d)
    print(product_fraction.denominator)  
