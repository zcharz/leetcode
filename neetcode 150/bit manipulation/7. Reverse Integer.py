class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2147483648
        MIN = -2147483647
        count, res = 0, 0
        neg = True if x<0 else False
        x = abs(x)
        
        while x:
            if count == 9:
                if res > MAX//10: 
                    return 0
                elif res == MAX//10 and neg and x%10 > MAX%10:
                    return 0
                elif res == MAX//10 and x%10 > MIN%10 :
                    return 0

            res = res*10 + x%10
            x = x//10
            count+=1

        return res if not neg else -res
    

sol = Solution()

x = 123
print(sol.reverse(x))

x = -123
print(sol.reverse(x))