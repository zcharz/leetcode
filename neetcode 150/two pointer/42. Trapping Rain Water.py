class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height)-1
        maxl, maxr = 0, 0
        total = 0

        while l<=r:
            if maxl<maxr:
                total+=max(0, min(maxl, maxr)-height[l])
                maxl = max(maxl, height[l])
                l+=1
            else:
                total+=max(0, min(maxl, maxr)-height[r])
                maxr = max(maxr, height[r])
                r-=1
        return total


height = [0,1,0,2,1,0,1,3,2,1,2,1]
# expected output: 6
sol = Solution()
print(sol.trap(height))