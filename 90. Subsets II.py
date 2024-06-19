# time complexity analysis:
# a value can be chosen or not (2)
# there are n values to choose or not (n)
# 2^n -> subsets
# each subset is max length n
# total time O(n*2^n)
# time complexity is the same regardless of duplicate skipping
# in the worst case


# the reason why skipping all instances of this number works:
# the branch that takes the first instance of the number will 
# include all possible combinations with duplicates of a particular number
# so skipping one -> skip all to avoid duplicates 


def subsetsWithDup(nums: list[int]) -> list[list[int]]:
    ret = []
    stack = []

    nums.sort()

    def backtrack(curr):
        if curr==len(nums):
            ret.append(stack.copy())
            return        
        
        # taking the current number
        stack.append(nums[curr])
        backtrack(curr+1)
        stack.pop()
        
        # not taking the current number
        # skip all instances of this number
        curr_num = nums[curr]
        # techincally don't need extra variable, can be done as 
        # nums[curr] == nums[curr+1]
        # but O(1) memeory is negligible

        # skips at least 1 number and more if there are duplicates
        while curr<len(nums) and nums[curr]==curr_num:
            curr+=1
        backtrack(curr)

    backtrack(0)
    return ret



# solution skipping duplicates only at placement time
# 
# def subsetsWithDup(nums: list[int]) -> list[list[int]]:
#     ret = []
#     stack = []

#     nums.sort()

#     def backtrack(curr):
#         if curr==len(nums) and stack not in ret:
#             ret.append(stack.copy())
#             return
#         elif curr==len(nums):
#             return
        
#         stack.append(nums[curr])
#         backtrack(curr+1)
#         stack.pop()
        
#         backtrack(curr+1)
    
#     backtrack(0)
#     return ret


test = [1,2,2]
print(subsetsWithDup(test))