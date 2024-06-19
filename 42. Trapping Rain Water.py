# idea: "precompute" each individual position
# rather than finding a dip then calculating the area
# this only works because moving the lower point guarentees 
# the next value, if lower (would store water), 
# will always have the right value (difference between lower height and itself)


# start from left and right
# iterate the side with the shorter height
# since if there new value is shorter, it will always have the same value


def trap(height: list[int]) -> int:
    l, r = 0, len(height)-1
    leftmax, rightmax = height[l], height[r]
    total = 0

    while l<r:
        if leftmax < rightmax:
            l+=1
            if height[l]<leftmax:
                total+=leftmax-height[l]
            else:
                leftmax = height[l]
        else:
            r-=1
            if height[r]<rightmax:
                total+=rightmax-height[r]
            else:
                rightmax = height[r]

    return total


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))