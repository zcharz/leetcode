class Solution:
    def countBits(self, n: int) -> list[int]:
        ret = [0]
        offset = 1
        for i in range(1,n+1):
            if i == offset: offset*=2
            ret.append(1+ret[i-offset])
        return ret


sol = Solution()
print(sol.countBits(2))
print(sol.countBits(5))
print(sol.countBits(16))