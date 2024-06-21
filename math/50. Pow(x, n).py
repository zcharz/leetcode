def myPow(x: float, n: int) -> float:
    def helper(x, c):
        if n == 0:
            return 1
        if x == 0:
            return x
        ret = helper(x * x, n//2)
        return x*ret if c%2 else ret

    ret = helper(x, abs(n))
    return ret if n>=0 else 1/ret
    

x = 2.00000
n = 10

print(myPow(x,n))