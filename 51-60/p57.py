from fractions import Fraction

def continued_frac(n):
    """
    yields the Fraction form of the first n 
    continued fractions of the square root of two
    """
    frac = 1 + Fraction(1,2)
    
    for _ in range(n):
        frac = 1 + 1/(1 + frac)
        yield frac

        
if __name__ == "__main__":
    
    num_fractions = int(input())
    
    long_numerator = [
        len(str(cf.numerator)) > len(str(cf.denominator)) 
        for cf in continued_frac(num_fractions)
    ]
    
    print(sum(long_numerator))

