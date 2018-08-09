from collections import deque
from sympy import primefactors

def prime_factor_sequence(seq_len):
    """
    Returns a list of consecutive integers of length seq_len
    each integer in the list has precisely seq_len prime divisors
    """
    
    lst = deque(range(1, seq_len+1))
    num_factors = deque(primefactors(i) for i in lst)
    target_factors = deque(seq_len for _ in range(seq_len))
    largest_num = lst[-1] + 1
    
    while True:

        #get rid of the oldest term
        lst.popleft()
        lst.append(largest_num)

        #add the new term
        num_factors.popleft()
        num_factors.append(len(primefactors(largest_num)))

        #check if the new_term works, if it does we're all finished
        if num_factors == target_factors:
            return lst
        
        #increment the current largest element
        largest_num += 1
if __name__ == "__main__":
    sequence_length = int(input())
    print(prime_factor_sequence(sequence_length))