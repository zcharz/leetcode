def hammingWeight(n: int) -> int:
    # O(32) constant time
    c = 0
    while n!=0:
        c+=n%2
        n = n>>1
    return c

    # the trick solution
    # still O(1)
    c = 0
    # n!=0
    while n:
        c+=1
        n = n&(n-1) # n &= (n-1)
        # bitwise and
    return c
