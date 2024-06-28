class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height)-1
        lmax, rmax = height[l], height[r]
        total = 0

        while l<r:
            if lmax<=rmax: 
                l+=1
                total+=max(lmax-height[l],0)
                lmax = max(lmax, height[l])
            else:
                r-=1
                total+=max(rmax-height[r], 0)
                rmax = max(rmax, height[r])

        return total


height = [0,1,0,2,1,0,1,3,2,1,2,1]
# expected output: 6
sol = Solution()
print(sol.trap(height))