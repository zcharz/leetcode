# always shift the shorter one???
# shift out to in

def maxArea(height: list[int]) -> int:
    l,r = 0, len(height)-1
    area = 0

    while l<r:
        new = (r-l)*min(height[l],height[r])
        area = max(area, new)
        if height[r]>height[l]: l+=1
        else: r-=1
    return area
