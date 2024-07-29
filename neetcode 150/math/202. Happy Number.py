class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def sumOfSquares(num):
            temp = 0
            while num:
                temp += (num%10)**2
                num -= num%10
                num //= 10
            return temp

        while n!=1:
            n = sumOfSquares(n)
            if n in seen: return False
            seen.add(n)
        return True


sol = Solution()

n = 19
print(sol.isHappy(n))

n = 2
print(sol.isHappy(n))