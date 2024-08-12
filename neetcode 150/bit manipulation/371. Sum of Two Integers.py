class Solution:
    def getSum(self, a: int, b: int) -> int:
        ret = 0
        curr = 1
        carry = 0

        while a or b:
            if a & 1 and b & 1 and carry:
                ret = ret | curr
                carry = 0
            elif (a & 1 and carry) or (b & 1 and carry) or (a & 1 and b & 1):
                carry = 1
            elif a & 1 or b & 1 or carry:
                ret = ret | curr
                carry = 0

            print(curr, a&1, b&1, carry, ret)

            curr = curr << 1
            a = a >> 1
            b = b >> 1

        return ret
    
sol = Solution()

# a, b = 1, 2
# print(sol.getSum(a, b))

a, b = 2, 3
print(sol.getSum(a, b))