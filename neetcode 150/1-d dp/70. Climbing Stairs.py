class Solution:
    def climbStairs(self, n: int) -> int:
        n1, n2 = 0, 1

        for i in range(n):
            # new = n1+n2
            # n1 = n2
            # n2 = new

            # shorthand with 2 lines
            # n1 = n1 + n2
            # n1, n2 = n2, n1

            # shorthand with 1 line
            n1, n2 = n2, n1+n2
        return  n2


sol = Solution()

n = 2
print(sol.climbStairs(n))

n = 3
print(sol.climbStairs(n))