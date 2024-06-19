def maxProfit(prices: list[int]) -> int:
    l, r = 0, 1
    maxP = 0

    while r<len(prices):
        #profitable
        if prices[r]>prices[l]:
            profit = prices[r]-prices[l]
            maxP = max(profit, maxP)

        #new low    
        else:
            l = r
        r+=1
        # r = l + 1

    return maxP


prices = [7,1,5,3,6,4]
print(maxProfit(prices))