class Solution:
    def reverseBits(self, n: int) -> int:
        ret, place = 0, 0
        while n!= 0:
            if n&1:
                ret+=2**(31-place)        
            place+=1
            n = n>>1
        return ret


sol = Solution()

n = 0b00000010100101000001111010011100
print(sol.reverseBits(n))

n = 0b11111111111111111111111111111101
print(sol.reverseBits(n))