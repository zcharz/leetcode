# still a bruteforce solution -> O(N*N)
# accounts for duplicates
def twoSum(numbers: list[int], target: int) -> list[int]:
    for i in range(len(numbers)-1):
        if i>0 and numbers[i] == numbers[i-1]:
            continue
        for j in range(i+1, len(numbers)):
            if numbers[i]+numbers[j] == target:
                return [i+1, j+1]
            

# two pointer solution
# O(N)
def twoSum(numbers: list[int], target: int) -> list[int]:
    p1, p2 = 0, len(numbers)-1
    while True:
        c = numbers[p1]+numbers[p2]
        if  c == target:
            return  [p1+1, p2+1]
        if c> target:
            p2-=1
        else:
            p1+=1
