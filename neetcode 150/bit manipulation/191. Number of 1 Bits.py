class Solution:
    # O(32) solution
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n&1: count += 1
            n = n>>1
        return count
    
    # "trick" to get rid of one 1 bit each time
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count+=1
            n = n & (n-1)
        return count
    



sol = Solution()

n = 11
print(sol.hammingWeight(n))

# n = 128
# print(sol.hammingWeight(n))