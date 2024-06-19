
# recursive backtracking solution
# runs out of time (TLE)
def canJump(nums: list[int]) -> bool:
    def dfs(pos, maxpos):
        if pos >= len(nums)-1:
            return True

        curr = nums[pos]
        if pos+curr<maxpos:
            return False
        
        maxpos = pos+curr
        
        for i in range(curr, 0, -1):
            temp = dfs(pos+i, maxpos)
            if temp:
                return True
            # this doesnt time out but only works because its wrong
            # return dfs(pos+i)

        return False
    
    return dfs(0, 0)


# iterateive O(n) solution
# iterate from the back
# find index 
def canJump(nums: list[int]) -> bool:
    max_reached = len(nums)-1

    for i in range(len(nums)-1, -1, -1):
        if i+nums[i]>=max_reached:
            max_reached = i
    
    if max_reached == 0:
        return True
    return False


test = [2,3,1,1,4]
test = [2,5,0,0]
# test = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]

print(canJump(test))
