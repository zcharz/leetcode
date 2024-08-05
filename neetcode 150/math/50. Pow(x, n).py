class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(i):
            if i == 0: return 1
            res = helper(i//2)
            res *= res
            return res*x if i%2 else res
        return helper(abs(n)) if n>0 else 1/helper(abs(n))



sol = Solution()
x = 2.00000
n = 10
print(sol.myPow(x, n))

# x = 2.00000
# n = -2
# print(sol.myPow(x, n))