# Find numbers n such that the sum of the factorail of the digits is equal to n.
# In order for a number, say with k digits, to have this property
# n = a_1a_2...a_k = a_1! + a_2! + ... + a_k! >= k and n <= 9!*k

#note now that 9! * 8 has seven digits, so if you have a eight digit number
# adn you take the sum  of the factorial of the digits it will be at most
#9! * 8, so will NOT be one of the numbers we're looking for. This argument
# for all numbers with more than eight digits, ie no number with more than 8
# digits has this property.



from math import factorial


def fact_digits():
    fac_pre = {str(i):factorial(i) for i in range(10)}
    total_sum = 0

    #we're starting the range here at 3 purely because of the fact that
    #the problem statement says to exclude 1! = 1 and 2! = 2
    for n in range(3,10**7):
        n = str(n)
        sum_n = sum(fac_pre[i] for i in n)
        n = int(n)
        if n == sum_n:
            total_sum += n

    return total_sum

if __name__ == '__main__':
    print(fact_digits())
