class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        ind = len(digits)-1
        carry = 1

        while carry and ind>=0:
            digits[ind] = (digits[ind] + carry)%10
            carry = 1 if digits[ind] == 0 else 0
            ind-=1

        return digits if not carry else [1]+digits


sol = Solution()

digits = [1,2,3]
print(sol.plusOne(digits))

digits = [9]
print(sol.plusOne(digits))