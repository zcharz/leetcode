class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t): return ''
        
        count = dict()
        chars = set(t)  
        for c in t:
            count[c] = count.get(c, 0) +1 

        curr = dict()
        l, r = 0, 0
        match = 0
        substart, subend = 0, 0
        
        while r<len(s):
            if s[r] not in chars:
                r+=1
                continue
            
            # s[r] in char, add to curr
            # if count of s[r] == count of char in t, plus match
            curr[s[r]] = curr.get(s[r], 0)+1
            if curr[s[r]] == count[s[r]]: match +=1

            # while for all diff chars in t, current l to r substring contains equal or more elements -> matches = len(chars)
            # move left until this condition would be invalidated
            while match==len(chars): 
                # print(f'shifting left: {l}, {r}, {s[l:r+1]}')
                if s[l] in chars and curr[s[l]] > count[s[l]]:
                    curr[s[l]] -= 1 
                # moved l as much as possible without reducing matches
                elif s[l] in chars and curr[s[l]] == count[s[l]]:
                    # print(f'break: {l}, {r}, {s[l:r+1]}')
                    # print(count, curr)
                    if subend-substart > r+1-l or substart==subend==0:
                        substart, subend = l, r+1
                    break
                # increment l if s[l] is not in t or curr[s[l]] is greater than needed
                l+=1
            r+=1

        return s[substart:subend] if not substart==subend==0 else ''


sol = Solution()

s = "ADOBECODEBANC"
t = "ABC"
print(sol.minWindow(s,t))