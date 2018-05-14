#looking at a 2n+1 size spiral, add up all the diagonal terms
#the formula works like this
#the top right hand corner is (2*n+1)**2
#the top left hand corner is 2*n units to the left, so (2*n+1)**2 - 2*n
#the bottom left hand corner is 2*n units below that, so (2*n+1)**2 - 4*n
#the bottom right hand corner is 2*n units to the right of
#that, so (2*n+1)**2 - 6*n

#summing those terms we get  4*(2*n+1)**2 - 12*n
#then you need to add in the inner terms

def diag_sum(n):
    if n == 0:
        return 1
    else:
        return 4*(2*n+1)**2 - 12*n + diag_sum(n-1)

if __name__ == '__main__':
    #for a 1001 array, n = 500
    n = int(input("n = "))
    print(diag_sum(n))
