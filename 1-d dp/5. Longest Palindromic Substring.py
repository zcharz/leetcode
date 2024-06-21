
# remember that dynamic programming serves to reduce repeated work


def longestPalindrome(s: str) -> str:


    if len(s)==1:
        return s


    dp = [i for i in s]

    # iterate diagonally 
    for length in range(len(s)):
        for start in range(len(s)):
            if start+length<len(s):


    print(dp)

    return dp[0]




def isPalindrome(s):
    l, r = 0, len(s)-1

    while l<r:
        if s[l]!=s[r]:
            return 1
        l+=1
        r-=1
    return len(s)



test = 'hello'

print(longestPalindrome(test))