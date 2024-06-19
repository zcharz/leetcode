# FIND k
# 0 < k <= max (piles)

# h >= len(piles)
# worst case h = len(piles), k = max(piles)



import math


def minEatingSpeed(piles: list[int], h: int) -> int:
    l, r = 1, max(piles)


    def canFinish(k) -> bool:
        c = 0

        # add the number of times it takes to finish this pile
        for i in piles:
            c+=math.ceil(i/k)

        if c<=h:
            return True
        return False



    while l<r:
        mid = (l+r)//2

        # print(range(l,r))
        # print(f'left = {l}   right = {r}    mid = {mid}     canfinish = {canFinish(mid)}')

        # if mid can finish, any value k equal or higher than mid can also finish
        if canFinish(mid):
            r = mid
       
        # if mid can't finish, only higher values of k can finish
        else:
            l = mid+1
        
    return l





test = [3,6,7,11]
h = 8


print(minEatingSpeed(test, 8))