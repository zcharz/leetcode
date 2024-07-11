class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # O(n) sliding size 3 windows
        count, curr = [0]*26, [0]*26
        for i in range(len(s1)):
            count[ord(s1[i])-ord('a')]+=1
            curr[ord(s2[i])-ord('a')]+=1

        matches = 0
        for i in range(26):
            matches +=1 if curr[i]==count[i] else 0

        for i in range(len(s2)-len(s1)):
            if matches == 26: return True
            
            # O(26) checking operation
            # if curr == count:
            #     return True
            # curr[l]-=1
            # curr[r]+=1

            l, r = ord(s2[i])-ord('a'), ord(s2[i+len(s1)])-ord('a')

            # decrementing matches if current left count and right count is a match
            # since those character counts will change
            if curr[l] == count[l]: matches-=1
            if curr[r] == count[r]: matches-=1

            curr[l]-=1
            curr[r]+=1

            # incrementing matches if new left count and new right count is a match
            if curr[l] == count[l]: matches+=1
            if curr[r] == count[r]: matches+=1
            
        return matches == 26


        # O(26n) with skips using 2 pointer (variable window size)
        l, r = 0, 0
        count, curr = [0]*26, [0]*26
        for c in s1:
            count[ord(c)-ord('a')]+=1
    
        while r<len(s2):
            ind = ord(s2[r])-ord('a')
            # if current character is not found in s1 at all
            # start iterating from the next character
            if count[ind] == 0:
                l=r+1
                r = l
                curr = [0]*26
                continue

            # current character is in s1, add to running count
            curr[ind]+=1

            # if current window is less than length of s1, keep shifting right
            if r-l<len(s1)-1:
                r+=1
                continue
            
            # if current window is equal length, check if number of counts are correct
            if curr == count: return True
            
            # if number of counts are not correct, shift left by 1
            curr[ord(s2[l])-ord('a')]-=1
            l, r = l+1, r+1

        return False


sol = Solution()

s1 = "ab"
s2 = "eidbaooo"
print(sol.checkInclusion(s1, s2))

s1 = 'adc'
s2 = 'dcda'
print(sol.checkInclusion(s1, s2))