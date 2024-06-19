# probably is a pointer/stack based solution as well
# def permute(nums: list[int]) -> list[list[int]]:
#     ret = []
#     stack = []

#     def backtrack(curr):
#         if len(stack)==len(nums):
#             ret.append(stack.copy())

        # something here 
#         stack.append(nums[curr])
#         backtrack(curr+1)
#         stack.pop()

#         backtrack(curr)
    

#     backtrack(0)
#     return ret



# slightly scuffed solution
#      N ... N-1 ... N-2 ... 1 -> O(N^N)
# since each recursive call is O(N) with for loop
# could be improved to O(N!) time 
# using an available list to loop over
# which decreases recursive call to O(1) time

def permute(nums: list[int]) -> list[list[int]]:
    ret = []
    stack = [None for i in range(len(nums))]

    def backtrack(curr, length):
        if length==len(nums):
            ret.append(stack.copy())
            return
        
        # for every index tahts not taken already:
        for i in range(len(stack)):
            if stack[i] != None:
                continue
            stack[i] = nums[curr]
            backtrack(curr+1,length+1)
            stack[i] = None
    
    backtrack(0,0)
    return ret

nums = [1,2,3]
print(permute(nums))