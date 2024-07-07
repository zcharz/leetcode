class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height)-1
        ret = 0

        while l<r:
            ret = max(ret, min(height[l], height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
                continue
            r-=1

        return ret
    

sol = Solution()

height = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height))