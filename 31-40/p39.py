def find_triangles(p):
    """
    For p>=3, counts the number of triples (a,b,c)
    with a+b+c=p and a^2+b^2=c^2.
    """
    counter = set() 
    for a in range(1,p):
        b = (2*a*p - p**2)/(2*(a-p))
        if b == int(b) and b > 0: 
            counter.add(frozenset({a,b}))
    return len(counter)



if __name__ == "__main__":
    p = int(input())
    max_p, max_solns = 3,0
    for i in range(3,p+1):
        tmp_solns = find_triangles(i)
        if tmp_solns > max_solns:
            max_p, max_solns = i, tmp_solns
        
    print(max_p)


