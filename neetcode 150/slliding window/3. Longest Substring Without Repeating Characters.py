def lengthOfLongestSubstring(s: str) -> int:

    if len(s)==1:
        return 1
    
    cmax = 0
    seen = dict()
    p = 0

    while p<len(s):

        if s[p] in seen.keys():
            # this ends a substring
            length = len(seen.keys())
            if length>cmax:
                cmax=length

            # reset position to right after first instance of duplicate
            p = seen[s[p]]+1
            seen = dict()

            # THIS IS INCORRECT AND NOT A PROPER SLIDING WINDOW
        
        else:
            seen[s[p]]=p
            p+=1

        # print(f'{p}   {seen}')
    
    # end of iteration substring
    if len(seen)>cmax:
        print(seen)
        return len(seen)

    return cmax
        


# test = "pwwkew"
test = 'aab'
test = "dvdf"

print(lengthOfLongestSubstring(test))



# neetcode solution
# more concise and proper sliding window

def lengthOfLongestSubstring(self, s: str) -> int:
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):

        # slide window until duplicate isnt in the substring
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])

        res = max(res, r - l + 1)
    return res