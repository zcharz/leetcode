# O(N) iteration
# keep the furthest jump at each step

def jump(nums: list[int]) -> int:
    count = 0
    max_dist = 0
    curr_dist = 0
    step = 0

    for i in range(len(nums)):
        if max_dist>=len(nums)-1:
            return count
        curr = i+nums[i]

        # print(f'{i}  {i+nums[i]}')

        if i==step:
            max_dist = max(curr_dist, curr)
            count+=1
            curr_dist = i
            step = max_dist
            continue

        curr_dist = max(curr, curr_dist)        


# nums = [2,3,1,1,4]
# nums = [3,2,1]
# nums = [2,3,0,1,4]
nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
print(jump(nums))