#all hexagonal numbers are triangular, so only really need to check if the
#numbers are hex and pent (triangular is free). We'll generate the hex numbers
#and just check if they're pentagonal

def is_pentagonal(P):
    """
    Returns True if P is pentagonal,
    returns False otherwise
    """
    tmp = (1+(1+24*P)**.5)/6
    return tmp == int(tmp)


def hex_gen(start_index):
    """
    generate hexagonal numbers starting at the start_index
    pentagonal number
    """
    index = start_index
    while True:
        hex_num = index*(2*index-1)
        index += 1
        yield hex_num

        
def next_hex_pent(hex_start_index):
    """
    finds the next number that is hexagonal, pentagonal,
    and triangular, starting at the hex_start_index-th hex number
    """
    hex_iter = hex_gen(hex_start_index)
    while True:
        hex_num = next(hex_iter)
        if is_pentagonal(hex_num):
            return hex_num
        
    
if __name__ == "__main__":
    hex_start_index = int(input())
    print(next_hex_pent(hex_start_index))