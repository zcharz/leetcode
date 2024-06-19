def containsDuplicate(nums: list[int]) -> bool:

    # return len(set(nums))!=len(nums)

    s = set()
    
    for element in nums:
        if element in s:
            return True
        s.add(element)
    return False